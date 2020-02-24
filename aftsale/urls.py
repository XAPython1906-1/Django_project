from django.urls import path
from . import views

urlpatterns = [
    path('all_evaluates/', views.all_evaluate),
    path('all_complaint/', views.all_complaint),
    path('new_complaint/', views.new_complaint),
]