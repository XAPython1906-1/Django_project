from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.all_ticket),
    path('partners/', views.all_partner),
    path('remove_partner/', views.remove_partner),
    path('my_ticket/', views.my_ticket),
    path('shenhe/', views.shenhe),
    path('remove_ticket/', views.remove_ticket),
    path('new_ticket/', views.new_ticket),
    path('one_ticket/<str:ticket_id>/', views.one_ticket),
    path('edit_ticket/<str:ticket_id>/', views.edit_ticket),

]
