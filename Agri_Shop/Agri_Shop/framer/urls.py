from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home Page
    path('', home, name='home'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('about', about, name='about'),

    path('logout', logout, name='logout'),
    path('profile/(?P<user>.*)/$', profile, name='profile'),
    path('dashboard/(?P<user>.*)/$', dashboard, name='dashboard'),
    path('receptionist_dashboard/(?P<user>.*)/$', receptionist_dashboard, name='receptionist_dashboard'),
    path('create_appointment/(?P<user>.*)/$', create_appointment, name='create_appointment'),
    path('delete_patient/(?P<id>\d+)/$', delete_patient, name='delete_patient'),
    path('update_patient/(?P<id>\d+)/$', update_patient, name='update_patient'),

    path('create_patient/', create_patient, name='create_patient'),
    path('myappointment/', myappointment, name='myappointment'),
    path('docter_appointment/', docter_appointment, name='docter_appointment'),
    path('docter_prescription/', docter_prescription, name='docter_prescription'),
    path('create_prescription/', create_prescription, name='create_prescription'),
    path('medical_history/', medical_history, name='medical_history'),
    path('update_status/(?P<id>\d+)/$', update_status, name='update_status'),
    path('hr_dashboard/', hr_dashboard, name='hr_dashboard'),
    path('hr_accounting/', hr_accounting, name='hr_accounting'),
    path('update_docter/(?P<id>\d+)/$', update_docter, name='update_docter'),
    path('delete_docter/', delete_docter, name='delete_docter'),
    path('patient_invoice/', patient_invoice, name='patient_invoice'),
    path('get_pdf/(?P<id>\d+)/$', get_pdf, name='get_pdf'),
    path('send_reminder/(?P<id>\d+)/$', send_reminder, name='send_reminder'),

]
