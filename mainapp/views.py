import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from common import md5_
from .models import *

from fms import settings

# Create your views here.


def login(request):
    # 分两种用户，一个是会员，一个管理员（系统）
    if request.method == 'POST':
        error = None

        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        remeber = request.POST.get('remeber', '')  # checkbox

        password_ = md5_.hash_encode(password)  # 转成md5后的密文

        # 验证用户名和口令是否为空
        if not all((username, password)):
            error = f'用户名或口令不能为空！'

        login_user = User.objects.filter(username=username, password=password_, status=1).first()
        if login_user:
            # 系统管理员
            login_info = {
                '_id': login_user.user_id,
                'name': login_user.username,
                'code': '666'
            }

        else:
            login_user = User.objects.filter(username=username, password=password_, status=2).first()
            if login_user:
                # 会员
                login_info = {
                    '_id': login_user.user_id,
                    'name': login_user.username,
                    'code': '777',
                }
            else:
                error = f'{username} 用户名或口令错误！'

        if not error:
            request.session['login_user'] = login_info
            return redirect('/')

    return render(request, 'login.html', locals())


def logout(request):
    del request.session['login_user']
    return redirect('/login/')


def index(request):
    return render(request, 'dashboard.html')

@csrf_exempt
def regist(request):
    if request.method == 'POST':
        error = None
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()

        password_ = md5_.hash_encode(password)  # 转成md5后的密文

        # 验证用户名和口令是否为空
        if not all((username, password)):
            error = f'用户名或口令不能为空！'

        repeat_user = User.objects.filter(username=username).first()
        if repeat_user:
            error = f'{username} 已存在，请重新填写用户名！'
        else:
            password_ = md5_.hash_encode(password)
            new_user = User(username=username, password=password_)
            new_user.save()
            return redirect('login/')

    return render(request, 'regist.html', locals())


def all_user_info(request):
    users = User.objects.filter(status=2)
    list(users)

    return render(request, 'all_userinfo.html', locals())

def message(request):
    return render(request, 'message.html')

