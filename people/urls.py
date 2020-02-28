from django.urls import path
from . import views

urlpatterns = [
    path('usersinfo/', views.all_user_info),
    path('allorder/', views.all_orders),
    path('myorder/', views.my_order),
    path('make_order/', views.make_order),
    path('remove_order/', views.remove_order),
    path('my/', views.my),
    path('edit_my/', views.edit_my),
    path('remove_user/', views.remove_user),
    path('remove_order/', views.remove_order)

]
