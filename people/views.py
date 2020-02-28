from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from partner.models import Partner
from .models import *

def all_user_info(request):
    # users = User.objects.filter(status=2)
    users = User.objects.all()

    return render(request, 'app/all_userinfo.html', locals())

def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'app/myorder.html', locals())


def my_order(request):
    user = request.session['login_user']
    user_id = user['_id']
    orders = Order.objects.filter(user_id=user_id)
    return render(request, 'app/myorder.html', locals())

@csrf_exempt
def make_order(request):
    if request.method == "POST":
        user_id = request.session['login_user']['_id']
        ticket = request.POST['ticket']
        number = request.POST['num']

        user = User.objects.filter(user_id=user_id)[0]
        ticket = TicketInfo.objects.filter(ticket_id=ticket)[0]

        order = Order(user_id=user, ticket_id=ticket, number=number)
        order.save()
        ticket.surplus -= int(number)
        ticket.save()

    return render(request, 'app/all_ticketinfo.html', locals())

@csrf_exempt
def remove_order(request):
    if request.method == "POST":
        queren = request.POST['queren']
        order = request.POST['order']
        if queren == "yes":
            order = Order.objects.filter(order_id=order)[0]

            order.status = 3
            order.save()

    return render(request, 'app/myorder.html', locals())

@csrf_exempt
def pay_order(request):
    if request.method == "POST":
        order_id = request.POST['order_id']
        order = Order.objects.filter(order_id=order_id)[0]
        order.status = 1
        order.save()
    return render(request, 'app/myorder.html', locals())


def my(request):
    user_id = request.session['login_user']['_id']
    my = User.objects.filter(user_id=user_id)[0]

    return render(request, 'app/my.html', locals())


@csrf_exempt
def edit_my(request):
    if request.method == "POST":
        user_id = request.session['login_user']['_id']
        status = int(request.POST['status'])
        xiugai = request.POST['xiugai']
        user = User.objects.filter(user_id=user_id)[0]
        if status == 1:
            user.username = xiugai
        elif status == 2:
            user.phone_number = xiugai
        elif status == 3:
            user.user_number = xiugai
        else:
            user.address = xiugai
        user.save()

    return render(request, 'app/my.html', locals())


@csrf_exempt
def remove_user(request):
    if request.method == "POST":
        queren = request.POST['queren']
        user = request.POST['user']
        if queren == "yes":
            user = User.objects.filter(user_id=user)[0]


            user.delete()

            result = {
                'code': '200',
                'status': 'success',
                'user_id':  user.user_id,
                'type': 'remove_user'
            }
            return JsonResponse(result)
    result = {
        'code': '300',
        'status': 'field',
        'user_id':  None,
        'type': 'remove_user'
    }
    return JsonResponse(result)


@csrf_exempt
def remove_order(request):
    if request.method == "POST":
        queren = request.POST['queren']
        order = request.POST['order']
        if queren == "yes":
            order = Order.objects.filter(order_id=order)[0]

            order.delete()

            result = {
                'code': '200',
                'status': 'success',
                'user_id':  order.order_id,
                'type': 'remove_user'
            }
            return JsonResponse(result)
    result = {
        'code': '300',
        'status': 'field',
        'user_id':  None,
        'type': 'remove_user'
    }
    return JsonResponse(result)





