from django.shortcuts import render, redirect

from .models import *


def all_evaluate(request):
    evaluates = Evaluate.objects.all()

    return render(request, 'app/all_evaluates.html', locals())

def all_complaint(request):
    complaints = Complaint.objects.all()

    return render(request, 'app/all_complaints.html', locals())

def new_complaint(request):

    return render(request, 'app/new_complaint.html', locals())

