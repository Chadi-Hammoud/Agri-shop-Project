from django.shortcuts import render
from django.http import HttpResponse



# def Framer_LogIn(request):
#     return HttpResponse("Login Page")

def home(request):
    return render(request, 'farmer/login.html', {"user": None})


def Framer_ViewAllOrders(request):
    return HttpResponse("ViewAllOrders Page")


def Framer_UpdateOrderStatus(request):
    return HttpResponse("Login Page")

def Framer_ManageProducts(request):
    return HttpResponse("ManageProducts Page")

def Framer_CreateProduct(request):
    return HttpResponse("Create Products Page")