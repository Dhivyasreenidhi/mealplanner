from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import contact,UserProfile
from . import urls
def plannerex(request):
    template = loader.get_template('planner.html')
    return HttpResponse(template.render())
def Homepage(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def ind(request):
    mymembers = UserProfile.objects.all().values()
    template = loader.get_template("contactinformation.html")
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))

def ind1(request):
    members = contact.objects.all().values()
    template = loader.get_template("contactinfo.html")
    context = {
        'members': members,
    }
    return HttpResponse(template.render(context,request))
def addrecord1(request):
        a = request.POST["Name"]
        b = request.POST["PhoneNumber"]
        c = request.POST["Email"]
        d = request.POST["Message"]
        member = contact(Name = a,PhoneNumber = b,EmailId = c,Message = d)
        member.save()
        return HttpResponseRedirect(reverse('ind1'))
def addrecord(request):
        x = request.POST["name"]
        y = request.POST["email"]
        z = request.POST["password"]
        member = UserProfile(username=x, email=y, password=z)
        member.save()
        return HttpResponseRedirect(reverse('ind'))  # Redirect to the 'ind' view

def registerpage(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({},request))
def loginpage(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def thankyoupage(request):
    template = loader.get_template('thankyoupage.html')
    return HttpResponse(template.render())

# Create your views here.
