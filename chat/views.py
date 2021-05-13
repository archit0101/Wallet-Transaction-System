from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Destination,log
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def printlogin(request):
    return render(request,'login.html')
def printing(request,user):
    #Dest1=Destination()
    print(user.username)
    U=Destination.objects.get(username=user.username)
    bal=U.balance # get bal
    return render(request,'home.html',{'name':user.username,'balance':bal})

def Debit(request):
    #val1 = int(request.POST['num1'])
    usern=request.POST['book_token']
    recie=request.POST['num2']

    user=Destination.objects.get(username=usern)
    a=Destination.objects.filter(username=recie)
    if len(a) != 0 :
        reciever=Destination.objects.get(username=recie)
    else:
        messages.info(request,"The entered Reciever Name does not exists!!!")
        return printing(request,user)
    val1 = user.balance
    val2 = int(request.POST['num1'])
    val3 = reciever.balance + val2
    res = val1 - val2 # set bal
    if res <= 100:
        messages.info(request,"Cannot Debit! Minimum Balance needs to be maintained!!")
        return printing(request,user)
    user.balance=res
    reciever.balance=val3
    reciever.save()
    user.save()
    Lg=log()
    Lg.username=usern
    Lg.Transaction_Type="Debit"
    Lg.amount=val2
    Lg.save()
    LgC=log()
    LgC.username=recie
    LgC.Transaction_Type="Credit"
    LgC.amount=val2
    LgC.save()
    return printing(request,user) 

def Credit(request):
    #val1 = int(request.POST['num1'])
    usern=request.POST['book_token']
    user=Destination.objects.get(username=usern)
    val1 = user.balance
    val2 = int(request.POST['num1'])
    res = val1 + val2 # set bal
    user.balance=res
    user.save()
    Lg=log()
    Lg.username=usern
    Lg.Transaction_Type="Credit"
    Lg.amount=val2
    Lg.save()
    return printing(request,user)

def Login(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    #Verify from DB
    user = auth.authenticate(username=val1,password=val2)

    if user is None:
        messages.info(request,"user not found, Please register to continue!!")
        return redirect('/')
    auth.login(request,user)
    return printing(request,user)
def Register(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    val3 = request.POST['num3']
    if val2==val3:
        if User.objects.filter(username=val1).exists():
            messages.info(request,"username taken")
            return redirect('/')
        else:
            user=User.objects.create_user(username=val1,password=val2)
            user.save()
            Dest=Destination()
            Dest.username=val1
            Dest.balance=100
            Dest.save()
            messages.info(request,'User successfully Created!!...Please Login to continue!')
    else:
        messages.info(request,"password values do not match!!")
        return redirect("/")
    return redirect('/')
def logout(request):
    auth.logout(request)
    return redirect('/')

def Log(request):
    username = request.POST['num1']
    transactions=log.objects.filter(username=username)
    return render(request,'Log.html',{'transaction':transactions})