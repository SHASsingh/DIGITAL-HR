from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField()
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=30)

class JobSeeker(models.Model):
    applicantname=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    city=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(primary_key=True)
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=10)
    keyskills=models.TextField()
    dob=models.CharField(max_length=30)
    regdate=models.CharField(max_length=30)

class AdminLogin(models.Model):
    adminid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)