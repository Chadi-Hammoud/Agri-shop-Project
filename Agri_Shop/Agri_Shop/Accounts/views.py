from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to success page or login page
            return redirect('accounts:login') 
    else:
        form = UserCreationForm()
    return render(request, 'Accounts/signup.html', {'form': form})
    # if request.method =='POST':
    #     form =UserCreationForm(request.POST)
    #     if form.is_valid():
    #        form.save()
    #        #LOG THE USER
    #        return redirect('Accounts:login') 
    # else:  
    #     form = UserCreationForm()
    #     return render(request, 'accounts/signup.html',{'form': form})


def login_view(request):
    return render(request, 'accounts/login.html')