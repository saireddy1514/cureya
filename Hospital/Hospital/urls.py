"""Hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django_email_verification import urls as mail_urls
from myapp import views
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home" ),
    path('home/',views.home, name="home" ),
    path('doctor/',views.doctor, name="doctor" ),
    path('patient/',views.patient, name="patient" ),
    path('patientlogin/',views.patientlogin, name="patientlogin" ),
    path('patientregistration/',views.patientregistration, name="patientregistration" ),
    path('doctorlogin/',views.doctorlogin, name="doctorlogin" ),
    path('doctorregistration/',views.doctorregistration, name="doctorregistration" ),
    path('patienthome/',views.patienthome, name="patienthome" ),
    path('doctorhome/',views.doctorhome, name="doctorhome" ),
    path('email/',include(mail_urls)),
    path('sendEmail/',views.sendEmail,name="sendEmail"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),
    path('doctoractivate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.doctoractivate, name='doctoractivate'),
    path('send_otp/',views.sendOtp.as_view(),name="sendOtp"),
    path('phoneverify/<str:status>',views.phoneverify,name="phoneverify"),
    path('patientphoneverify/<str:status>',views.patientphoneverify,name="patientphoneverify"),


]
