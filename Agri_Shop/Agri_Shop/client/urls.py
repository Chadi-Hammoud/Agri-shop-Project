from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage,name = 'home'),
    path('cart/',views.cart , name = 'cart'),
    path('shop/',views.shop , name = 'shop'),
]
