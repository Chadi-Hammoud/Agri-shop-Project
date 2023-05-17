from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

def homePage(request):
    return render(request,'pages/index.html',{"user": None}) 
def cart(request):
    return render(request,'pages/cart.html')
def shop(request):
    return render(request,'pages/shop.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to success page or login page
            return redirect('accounts:login') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
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
    return render(request, 'registration/login.html')


def checkout_view(request):
    return render(request,'pages/checkout.html')