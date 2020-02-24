from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.all_ticket),
    path('partners/', views.all_partner),
    path('new_partner/', views.new_ticket),

    path('my_ticket/', views.my_ticket),

]