from django.shortcuts import render


def homePage(request):
    return render(request,'pages/index.html',{"user": None}) 
def cart(request):
    return render(request,'partiel/cart.html')
def shop(request):
    return render(request,'pages/shop.html')