from django.shortcuts import render
from django.http import HttpResponse
from .models import data

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def back(request):
    return render(request,'home.html')
def plum(request):
    return render(request,'plum.html')
def elec(request):
    return render(request,'electr.html')


def ele(request):
  if request.method=="POST":  
    name1=request.POST["name"]
    add1=request.POST["d_no"]
    add2=request.POST["s_name"]
    add3=request.POST["city"]
    add4=request.POST["district"]
    mob1=request.POST["mob1"]
    mob2=request.POST["mob2"]
    email=request.POST["email"]
    issue=request.POST["issue"]
    work='ELECTRICAL-WORK'
    context={
        'work':work,
        'user':name1,
        'dno':add1,
        'street':add2,
        'city':add3,
        'dis':add4,
        'mob1':mob1,
        'mob2':mob2,
        'mail':email,
        'issue':issue
    }
    obj=data()
    obj.work=work
    obj.name=name1
    obj.d_no=add1
    obj.s_name=add2
    obj.city=add3
    obj.district=add4
    obj.mobile_no=mob1
    obj.mobile_no2=mob2
    obj.mail_id=email
    obj.issue=issue
    obj.save()
    
    return render(request,'final.html',context)
  
def plumi(request):
  if request.method=="POST":  
    name1=request.POST["name"]
    add1=request.POST["d_no"]
    add2=request.POST["s_name"]
    add3=request.POST["city"]
    add4=request.POST["district"]
    mob1=request.POST["mob1"]
    mob2=request.POST["mob2"]
    email=request.POST["email"]
    issue=request.POST["issue"]
    work='PLUMBING-WORK'
    context={
        'work':work,
        'user':name1,
        'dno':add1,
        'street':add2,
        'city':add3,
        'dis':add4,
        'mob1':mob1,
        'mob2':mob2,
        'mail':email,
        'issue':issue
    }
    obj=data()
    obj.work=work
    obj.name=name1
    obj.d_no=add1
    obj.s_name=add2
    obj.city=add3
    obj.district=add4
    obj.mobile_no=mob1
    obj.mobile_no2=mob2
    obj.mail_id=email
    obj.issue=issue
    obj.save()
    return render(request,'final.html',context)