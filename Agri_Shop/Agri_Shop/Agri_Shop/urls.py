
from django.contrib import admin
from django.urls import path, include
# from . import views

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('home/',include('client.urls')),
]
