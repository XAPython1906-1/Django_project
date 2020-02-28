from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from people.models import *
from .models import *


def all_evaluate(request):
    evaluates = Evaluate.objects.all()

    return render(request, 'app/all_evaluates.html', locals())

def all_complaint(request):
    complaints = Complaint.objects.all()

    return render(request, 'app/all_complaints.html', locals())

@csrf_exempt
def new_complaint(request):
    if request.method == "POST":
        user_id = request.session['login_user']['_id']
        ticket = request.POST['ticket']
        text = request.POST['text']

        ticket = TicketInfo.objects.filter(ticket_id=ticket)[0]

        complaint = Complaint(ticket_id=ticket, text=text, comname=user_id)
        complaint.save()

    return render(request, 'app/new_complaint.html', locals())

@csrf_exempt
def new_evaluate(request):
    if request.method == "POST":
        order = request.POST['order']
        text = request.POST['text']

        order = Order.objects.filter(order_id=order)[0]

        evaluate = Evaluate(order_id=order, text=text)
        evaluate.save()

    return render(request, 'app/myorder.html', locals())

def my_evaluate(request):
    user_id = request.session['login_user']['_id']
    orders = Order.objects.filter(user_id=user_id)
    evaluates = []
    for order in orders:
        evaluates.append(Evaluate.objects.filter(order_id=order.order_id))
    evaluates = evaluates[:-1]

    return render(request, 'app/myevaluate.html', locals())

def my_complaint(request):
    user_id = request.session['login_user']['_id']
    complaints = Complaint.objects.filter(comname=user_id)

    # app/myevaluate.html
    return render(request, 'app/mycomplaint.html', locals())


@csrf_exempt
def reply_evaluate(request):
    if request.method == "POST":
        reply_user = request.session['login_user']['_id']
        evaluate = request.POST['evaluate']
        neirong = request.POST['neirong']

        reply_user = User.objects.filter(user_id=reply_user)[0]
        evaluate = Evaluate.objects.filter(evaluate_id=evaluate)[0]
        evaluate.reply_text = neirong
        evaluate.reply_people = reply_user.username

        evaluate.save()

        result = {
            'code': '200',
            'status': 'success',
            'user_id':  evaluate.evaluate_id,
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
def reply_complaint(request):
    if request.method == "POST":
        reply_user = request.session['login_user']['_id']
        complaint = request.POST['complaint']
        neirong = request.POST['neirong']

        reply_user = User.objects.filter(user_id=reply_user)[0]
        complaint = Complaint.objects.filter(complaint_id=complaint)[0]
        complaint.reply_text = neirong
        complaint.reply_people = reply_user.username

        complaint.save()

        result = {
            'code': '200',
            'status': 'success',
            'complaint_id':  complaint.complaint_id,
            'type': 'remove_user'
        }
        return JsonResponse(result)
    result = {
        'code': '300',
        'status': 'field',
        'complaint_id':  None,
        'type': 'remove_user'
    }
    return JsonResponse(result)

