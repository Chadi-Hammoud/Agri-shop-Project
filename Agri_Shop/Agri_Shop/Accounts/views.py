from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method =='POST':
        form =UserCreationForm(request.method)
        if form.is_valid():
           form.save()
           #LOG THE USER
           return redirect('pages/index.html') 
    else:  
        form = UserCreationForm()
        return render(request, 'accounts/signup.html',{'form': form})


def login_view(request):
    return render(request, 'accounts/login.html')