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
        print(ticket, text)
        ticket = TicketInfo.objects.filter(ticket_id=ticket)[0]

        complaint = Complaint(ticket_id=ticket, text=text, comname=user_id)
        complaint.save()

    return render(request, 'app/new_complaint.html', locals())

@csrf_exempt
def new_evaluate(request):
    if request.method == "POST":
        order = request.POST['order']
        text = request.POST['text']
        print(order, text)
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
    print(evaluates)

    return render(request, 'app/myevaluate.html', locals())

def my_complaint(request):
    user_id = request.session['login_user']['_id']
    complaints = Complaint.objects.filter(comname=user_id)
    print(complaints)

    # app/myevaluate.html
    return render(request, 'app/mycomplaint.html', locals())


