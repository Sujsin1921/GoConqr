from unicodedata import category
from django.db import models
from django.shortcuts import render
from django.contrib import messages 
from contextlib import contextmanager
from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q

# inmporting All Models
from .models import course
from .models import userprofill

# Create your views here.
def index(request):
    core = course.objects.filter(category ='backend')
    cou1 = course.objects.get(id=1)
    tech = course.objects.filter(category = 'framework')
    datab= course.objects.filter(category = 'database')
    params = {'core':core, 'tech':tech,'datab':datab}
    return render(request,"index.html",params)

def login(request):
    try:
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            user = userprofill.objects.get(email = username)
            print(user.password)
            if(user.password == password):
                request.session['bar'] = username
                return redirect("dashboard")
            else:
                messages.error(request,"username or password is invalid")
                return redirect("/")
    except:
        messages.error(request,"username or password is invalid")
        return redirect("/")
            
def logout(request):
    if 'bar' in request.session:
        del request.session['bar']
        messages.success(request,"Logged out!")
        return redirect('/')
    return "Error 404 Not Found"    

def dashboard(request):
    try:
        if 'bar' in request.session:
            user = request.session['bar']
            userpro = userprofill.objects.get(email=user)
            # filter for core tech
            coreall = course.objects.exclude(Q(language = 'python') | Q(language='java') | ~Q(category ='backend'))
            if(userpro.language == 'combo'):
                core = course.objects.filter(Q(language='python', category = 'backend') | Q(language='java',category = 'backend'))
            else:
                core = course.objects.filter(language = userpro.language, category = 'backend')

            tech =course.objects.filter(technology = userpro.technology, category = 'framework')
            techall =course.objects.exclude(Q(technology = userpro.technology) | ~Q(category = 'framework'))
            datab= course.objects.filter(category = 'database')
            params = {'core':core,'tech':tech, 'username':user,'datab':datab,'coreall':coreall,'techall':techall}
            return render(request,'dashboard.html',params)
        else:
            return redirect('/')
    except:
        return redirect('/')

def profill(request):
    if request.method == 'POST':
        gName = request.POST['username']
        gemail = request.POST['email']
        gpassword = request.POST['password']
        gbackground = request.POST['IT']
        glevel = request.POST['level']
        gcategory = request.POST['category']
        gfront = request.POST['front']
        glanguage = request.POST['language']
        gTechnology = request.POST['Technology']
        userprofill.objects.create(name = gName, email= gemail,password = gpassword,background = gbackground,category = gcategory, language = glanguage,front = gfront, level= glevel, technology = gTechnology)
        messages.warning(request,'Try Loging in with new credentials')
        return redirect('/')
    return "Error 404 page Not found"
        

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
