from django.shortcuts import render

from .models import *

def all_user_info(request):
    users = User.objects.filter(status=2)

    return render(request, 'app/all_userinfo.html', locals())

def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'app/myorder.html', locals())

def my_order(request):
    user = request.session['login_user']
    user_id = user['_id']
    orders = Order.objects.filter(user_id=user_id)

    return render(request, 'app/myorder.html', locals())



