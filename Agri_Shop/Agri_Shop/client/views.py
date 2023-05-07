from django.shortcuts import render


def client_login(request):
    return render(request,'pages/index.html',{"user": None}) 