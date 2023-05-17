from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import authenticate , login

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username,password=password)
            login(request,user)
            return redirect ('accounts/profile')
    else:
        form = SignUpForm()
    return render(request,'registration/signup.html',{'form':form})