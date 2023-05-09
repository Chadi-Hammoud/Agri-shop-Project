
from django.contrib import admin
from django.urls import path, include
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('farmer.urls')),
    path('client/',include('client.urls')),
    path('accounts/',include('Accounts.urls')),
]
