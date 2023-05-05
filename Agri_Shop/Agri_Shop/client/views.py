from django.shortcuts import render


def client_login(request):
    return render(request,'client/singup.html',{"user": None}) 