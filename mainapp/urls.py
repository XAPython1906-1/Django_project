#!/usr/bin/python3
# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('regist/', views.regist),
    path('partreg/', views.partner_regist),
    path('', views.index),
    path('help/', views.help),
    path('message/', views.message)
]
