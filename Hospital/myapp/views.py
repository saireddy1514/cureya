from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,JsonResponse
import mysql.connector
from operator import itemgetter
from django.contrib.auth import get_user_model
from django_email_verification import sendConfirm
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail,EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from twilio.rest import Client 
from rest_framework.views import APIView 
from django.core.mail import send_mail

import random
def home(request):
    return render(request,'home.html')
def patient(request):
    return render(request,'patient.html')
def doctor(request):
    return render(request,'doctor.html')
def patienthome(request):
    return render(request,'patienthome.html')
def doctorhome(request):

    return render(request,'doctorhome.html')

def patientregistration(request):
    if request.method == "POST":
        filledform = RegistrationData(request.POST)
        if filledform.is_valid():
            user = filledform.save(commit=False)
            user.is_active = False
            user.save()
            user.patid='C2'+str(user.id)
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('mail_body.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.email)),
                'token':account_activation_token.make_token(user),
            })
            to_email = filledform.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            form = RegistrationData()
            return render(request, "patientregistration.html",{
                'form':form,
                "successmessage":"Please confirm your email address to complete the registration"
            })
        else:
            form = RegistrationData()
            return render(request, "patientregistration.html",{
                'form':form,
                'message':"Please Try Again."
            })
    form = RegistrationData()
    return render(request, "patientregistration.html",{
        'form':form
    })

def activate(request, uidb64, token):
    try:
        email = force_text(urlsafe_base64_decode(uidb64))
        user = Registration.objects.get(email=email)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()     
        msg="Thank you for your email confirmation. Now you can login your account.  Your User ID is:- "+str(user.patid)
        send_mail(
    'Thank you for registering Cureya!!!',
    'Your User ID:-'+str(user.patid),
    'cureya@dummygmail.com',
    [user.email],
    fail_silently=False,
)
        return HttpResponse(msg)
    else:
        return HttpResponse('Activation link is invalid!')



def patientlogin(request):
    if request.method=='POST':
        email = request.POST['id']
        password = request.POST['password'] 
        user=Registration.objects.filter(patid=email,password=password)
        if len(user)==0:
            return HttpResponse('Invalid Email or password')
        else:
            if user[0].is_active==False:
                return HttpResponse('Please Confirm your mail')
            else:
                if user[0].mob_is_active==False:
                    verify=str(user[0].patid)+str(user[0].phoneno)
                    return render(request,'patienthome.html',{'email':user[0].email,'id':user[0].patid,'status':user[0].phoneno,'verify':verify})
                else:
                    verify=str(user[0].patid)+str(user[0].phoneno)
                    return render(request,'patienthome.html',{'email':user[0].email,'id':user[0].patid,'status':user[0].phoneno})
    return render(request,'patientlogin.html')


def doctorregistration(request):
    if request.method == "POST":
        filledform = DoctorRegistrationData(request.POST)
        if filledform.is_valid():
            user = filledform.save(commit=False)
            user.is_active = False
            user.save()
            user.docid='C1'+str(user.id)
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('doctor_mailbody.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.email)),
                'token':account_activation_token.make_token(user),
            })
            to_email = filledform.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            form = DoctorRegistrationData()
            return render(request, "doctorregistration.html",{
                'form':form,
                "successmessage":"Please confirm your email address to complete the registration"
            })
        else:
            form = DoctorRegistrationData()
            return render(request, "doctorregistration.html",{
                'form':form,
                'message':"Please Try Again."
            }) 
    form = DoctorRegistrationData()
    return render(request, "doctorregistration.html",{
        'form':form
    })

def doctoractivate(request, uidb64, token):
    try:
        email = force_text(urlsafe_base64_decode(uidb64))
        user = DoctorRegistration.objects.get(email=email)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        msg="Thank you for your email confirmation. Now you can login your account.  Your User ID is:- "+str(user.docid)
        send_mail(
    'Thank you for registering Cureya!!!',
    'Your User ID:-'+str(user.docid),
    'cureya@dummygmail.com',
    [user.email],
    fail_silently=False,
)
        return HttpResponse(msg)
    else:
        return HttpResponse('Activation link is invalid!')



def doctorlogin(request):
    if request.method=='POST':
        email = request.POST['username']
        password = request.POST['password'] 
        user=DoctorRegistration.objects.filter(docid=email,password=password)
        if len(user)==0:
            return HttpResponse('Invalid Email or password')
        else:
            if user[0].is_active==False:
                return HttpResponse('Please Confirm your mail')
            else:
                if user[0].mob_is_active==False:
                    verify=str(user[0].docid)+str(user[0].phoneno)
                    return render(request,'doctorhome.html',{'email':user[0].email,'id':user[0].docid,'status':user[0].phoneno,'verify':verify})
                else:
                    verify=str(user[0].docid)+str(user[0].phoneno)
                    return render(request,'doctorhome.html',{'email':user[0].email,'id':user[0].docid,'status':user[0].phoneno})
                    
    return render(request,'doctorlogin.html')


@csrf_exempt
def sendEmail(request):
    password=request.POST['password']
    username=request.POST['username']
    email=request.POST['email']
    user=get_user_model().objects.create(username=username,password=password,email=email)
    sendConfirm(user)
    return render(request,'confirm_template.html')

class sendOtp(APIView):
    def post(self,request,number):
        account_sid="AC4e1c0f151aad54b42edf505b6e88a931"
        auth_token="1f853f151b09a41d30af4982f52e4acc"
        client=Client(account_sid,auth_token)
        otp=generateOTP()
        body="Your OTP is "+str(otp)
        message=client.messages.create(to=number,from_="+18599037847",body=body)
        if message.sid:
            print("send succesfully")
            print(otp)
            return otp
        else:
            print("send failed")
            return 0

def generateOTP():
    return random.randrange(100000,999999)


def phoneverify(request,status):
    if request.method == "POST":
        num = request.POST["num"]
        id = request.POST["id"]
        otp = request.POST["otp"]
        user = OTPVerification.objects.filter(pid=id,otp=otp)
        if(len(user)==0):
            return render(request,'confirm_template.html',{'num':num})
        else:
            p=DoctorRegistration.objects.filter(docid=id).update(mob_is_active=True)
            q=DoctorRegistration.objects.filter(docid=id)
            r=OTPVerification.objects.filter(otp=otp).delete()
            return render(request,'doctorhome.html',{'email':q[0].email,'id':q[0].docid,'status':q[0].phoneno})                    
    s=sendOtp()
    status=str(status)
    id=status[:7]
    status=status[7:]
    num="+91"+str(status)
    h=sendOtp.post(s,request,num)
    if h==0:
        return HttpResponse("Failed to Send OTP")
    g=OTPVerification(phoneno=num,otp=h,pid=id)
    g.save()
    return render(request,'confirm_template.html',{'num':num,'id':id})


def patientphoneverify(request,status):
    if request.method == "POST":
        num = request.POST["num"]
        id = request.POST["id"]
        otp = request.POST["otp"]
        user = OTPVerification.objects.filter(pid=id,otp=otp)
        if(len(user)==0):
            return render(request,'confirm_template.html',{'num':num})
        else:
            p=Registration.objects.filter(patid=id).update(mob_is_active=True)
            q=Registration.objects.filter(patid=id)
            r=OTPVerification.objects.filter(otp=otp).delete()
            return render(request,'patienthome.html',{'email':q[0].email,'id':q[0].patid,'status':q[0].phoneno})                    
    s=sendOtp()
    status=str(status)
    id=status[:7]
    status=status[7:]
    num="+91"+str(status)
    h=sendOtp.post(s,request,num)
    if h==0:
        return HttpResponse("Failed to Send OTP")
    g=OTPVerification(phoneno=num,otp=h,pid=id)
    g.save()
    return render(request,'confirm_template.html',{'num':num,'id':id})
