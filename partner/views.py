from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

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

    return render(request, 'app/all_ticketinfo.html', locals())

@csrf_exempt
def remove_partner(request):
    if request.method == "POST":
        queren = request.POST['queren']
        partner = request.POST['partner']
        if queren == "yes":
            partner = Partner.objects.filter(partner_id=partner)[0]

            partner.delete()

            result = {
                'code': '200',
                'status': 'success',
                'user_id':  partner.partner_id,
                'type': 'remove_partner'
            }
            return JsonResponse(result)
    result = {
        'code': '300',
        'status': 'field',
        'user_id':  None,
        'type': 'remove_partner'
    }
    return JsonResponse(result)


@csrf_exempt
def shenhe(request):
    if request.method == "POST":
        queren = request.POST['queren']
        ticket = request.POST['ticket']
        if queren == "yes":
            ticket = TicketInfo.objects.filter(ticket_id=ticket)[0]

            if ticket.status == 3:
                ticket.status = 1
                ticket.save()

                result = {
                    'code': '200',
                    'status': 'success',
                    'user_id':  ticket.ticket_id,
                    'type': 'shenhe'
                }
                return JsonResponse(result)
    result = {
        'code': '300',
        'status': 'field',
        'user_id':  None,
        'type': 'shenhe'
    }
    return JsonResponse(result)

@csrf_exempt
def remove_ticket(request):
    if request.method == "POST":
        queren = request.POST['queren']
        ticket = request.POST['ticket']
        if queren == "yes":
            ticket = TicketInfo.objects.filter(ticket_id=ticket)[0]

            ticket.delete()
            result = {
                'code': '200',
                'status': 'success',
                'user_id':  ticket.ticket_id,
                'type': 'remove_ticket'
            }
            return JsonResponse(result)
    result = {
        'code': '300',
        'status': 'field',
        'user_id':  None,
        'type': 'remove_ticket'
    }
    return JsonResponse(result)


@csrf_exempt
def new_ticket(request):
    if request.method == "POST":
        partner_id = request.session['login_user']['_id']
        infoname = request.POST['infoname']
        tictype = request.POST['tictype']
        address = request.POST['address']
        time = request.POST['time']
        date = request.POST['date']
        price = request.POST['price']
        total = request.POST['total']
        partner = Partner.objects.filter(partner_id=partner_id)[0]
        datetime = date + " " + time

        ticket = TicketInfo(partner_id=partner, infoname=infoname,
                            tictype=tictype, address=address,
                            show_time=datetime, price=price,
                            total=total, surplus=total)
        ticket.save()

        return render(request, 'app/new_ticket.html', locals())

    return render(request, 'app/new_ticket.html', locals())


def one_ticket(request, ticket_id):
    ticket = TicketInfo.objects.filter(ticket_id=ticket_id)[0]
    date = str(ticket.show_time.date())
    time = ticket.show_time.time()
    print(date, time)

    return render(request, 'app/one_ticket.html', locals())


@csrf_exempt
def edit_ticket(request, ticket_id):
    user_id = request.session['login_user']['_id']
    infoname = request.POST['infoname']
    tictype = request.POST['tictype']
    address = request.POST['address']
    time = request.POST['time']
    date = request.POST['date']
    price = request.POST['price']
    total = request.POST['total']
    datetime = date + " " + time

    ticket = TicketInfo.objects.filter(ticket_id=ticket_id)[0]

    ticket.infoname=infoname
    ticket.tictype=tictype
    ticket.address=address
    ticket.show_time=datetime
    ticket.price=price
    ticket.total=total
    ticket.surplus=total

    ticket.save()
    tickets = TicketInfo.objects.filter(partner_id=user_id)
    result = {
        'code': '200',
        'status': 'success',
        'user_id':  ticket.ticket_id,
        'type': 'new_ticket'
    }
    return render(request, 'app/all_ticketinfo.html', locals())

