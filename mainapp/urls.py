#!/usr/bin/python3
# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('regist/', views.regist),
    path('', views.index),
    path('usersinfo/', views.all_user_info),
    path('message/', views.message)
]
