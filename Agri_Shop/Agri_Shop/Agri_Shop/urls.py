
from django.contrib import admin
from django.urls import path, include
# from . import views

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('Accounts.urls',namespace='accounts')),
    path('admin/', admin.site.urls),
    path('home/',include('client.urls')),
]
