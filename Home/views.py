from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from datetime import datetime
from Home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is homepage")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is about us")

def projects(request):
    return HttpResponse("This is projects file")

def contactus(request):
    if request.method =="POST":
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(email = email,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, " Thanks you for your Message!")

    context = {
        'alerttype':'success'
    }
    return render(request,'contactus.html',context)

def loginUser(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request,user)
            context = {
                'login_username':username
            }
            return render(request,"profile.html",context)
            # return redirect("/profile")
        else:
        # No backend authenticated the credentials
            context = {
                'alerttype':'danger'
            }
            messages.error(request, "No User Found!")
            return render(request,"login.html",context)
        
    return render(request,'login.html')


def logoutUser(request):
    # return render(request,'index.html')
    return redirect("/login")

def profile(request): 
    return render(request,"profile.html")