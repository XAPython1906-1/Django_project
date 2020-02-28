from django.urls import path
from . import views

urlpatterns = [
    path('all_evaluates/', views.all_evaluate),
    path('all_complaint/', views.all_complaint),
    path('new_complaint/', views.new_complaint),
    path('new_evaluate/', views.new_evaluate),
    path('my_evaluate/', views.my_evaluate),
    path('my_complaint/', views.my_complaint),
    path('reply_evaluate/', views.reply_evaluate),
    path('reply_complaint/', views.reply_complaint),
]
