from django.shortcuts import render, redirect

from .models import *


def all_ticket(request):
    tickets = TicketInfo.objects.all()

    return render(request, 'app/all_ticketinfo.html', locals())

def all_partner(request):
    partners = Partner.objects.all()

    return render(request, 'app/all_partner.html', locals())

def my_ticket(request):
    user = request.session['login_user']
    user_id = user['_id']

    tickets = TicketInfo.objects.filter(partner_id=user_id)
    print(tickets)

    return render(request, 'app/all_ticketinfo.html', locals())


def new_ticket(request):


    return render(request, 'app/new_ticket.html', locals())

def buy_ticket(request):
    pass