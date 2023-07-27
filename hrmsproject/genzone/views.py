from django.shortcuts import render,redirect,reverse
from .models import Enquiry,JobSeeker,AdminLogin
import datetime
from django.core.exceptions import ObjectDoesNotExist
from adminzone.models import Notification
from . import smssender
# Create your views here.
def index(request):
    nf=Notification.objects.all()
    return  render(request,"index.html",{'nf':nf})
def about(request):
    nf=Notification.objects.all()
    return render(request,"about.html",{'nf':nf})
def registration(request):
    nf=Notification.objects.all()
    return render(request,"registration.html",{'nf':nf})
def login(request):
    nf=Notification.objects.all()
    return render(request,"login.html",{'nf':nf})
def enquiry(request):
    nf=Notification.objects.all()
    return  render(request,"enquiry.html",{'nf':nf})
def saveenquiry(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    enquirydate=datetime.datetime.today()
    enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
    enq.save()
    smssender.sendsms(contactno,'thanks for your enquiry we will help u soon!')
    return redirect('index')
def jobseekerreg(request):
    applicantname=request.POST['applicantname']
    gender=request.POST['gender']
    address=request.POST['address']
    city=request.POST['city']
    country=request.POST['country']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    qualification=request.POST['qualification']
    experience=request.POST['experience']
    keyskills=request.POST['keyskills']
    dob=request.POST['dob']
    regdate=datetime.datetime.today()
    reg=JobSeeker(applicantname=applicantname,gender=gender,address=address,city=city,country=country,contactno=contactno,emailaddress=emailaddress,qualification=qualification,experience=experience,
                  keyskills=keyskills,dob=dob,regdate=regdate)
    reg.save()
    return redirect('index')
def validateuser(request):
    adminid=request.POST['adminid']
    password=request.POST['password']
    msg=''
    try:
        obj = AdminLogin.objects.get(adminid=adminid, password=password)
        if obj is not None:
            request.session['adminid']=adminid
            return redirect(reverse('adminzone:adminhome'))
    except ObjectDoesNotExist:
        msg="invalid user !"
    return render(request,"login.html",{'msg':msg})