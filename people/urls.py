from django.urls import path
from . import views

urlpatterns = [
    path('usersinfo/', views.all_user_info),
    path('allticket/', views.all_orders),
    path('myticket/', views.my_order)

]