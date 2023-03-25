from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Page1
from .models import About


# Create your views here.


def hello(request):
            template = loader.get_template('hello.html')
            return HttpResponse(template.render())
def index(request):
            template = loader.get_template('index.html')
            return HttpResponse(template.render())
def cm(request):
        template = loader.get_template('cm.html')
        return HttpResponse(template.render({}, request))

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse



    

def index(request):
    value = Page1.objects.last
    about=About.objects.last
    template = loader.get_template('index.html')
    context = {
        'values': value,
        'about':about
    }
    return HttpResponse(template.render(context, request))    

def addcm1(request):
        fname = request.POST['fname']
        lname = request.POST['lname']
        prof=request.POST['prof']
        logo=request.POST['logo']
        member = Page1(fname=fname, lname=lname, prof=prof,logo=logo)
        member.save()
        return HttpResponseRedirect(reverse('index'))



def cm_1_update(request):
        mymember = Page1.objects.last
        template = loader.get_template('cm_1_update.html')
        context = {
            'mymember': mymember,
        }
        return HttpResponse(template.render(context, request))



def updaterecord(request):
            fname = request.POST['fname']
            lname = request.POST['lname']
            prof=request.POST['prof']
            logo=request.POST['logo']
            member = Page1.objects.last()
            member.fname = fname
            member.lname = lname
            member.logo = logo
            member.prof = prof
            member.save()
            return HttpResponseRedirect(reverse('index'))



#About Page



def about_add(request):
        template = loader.get_template('about_add.html')
        return HttpResponse(template.render({}, request))

def about_add_do(request):
            fname = request.POST['fname']
            lname = request.POST['lname']
            prof=request.POST['prof']
            age=request.POST['age']
            ffrom=request.POST['from']
            live=request.POST['live']
            gender=request.POST['gender']
            about1=request.POST['about']
          
            about = About(fname = fname,
            lname = lname,
            prof = prof,
            about = about1,
            ffrom=ffrom,
            age = age,
            live= live,
            gender = gender)
            about.save()
            return HttpResponseRedirect(reverse('index'))


def about_update(request):
        about = About.objects.last
        template = loader.get_template('about_update.html')
        context = {
            'about': about,
        }
        return HttpResponse(template.render(context, request))

def about_update_do(request):
            fname = request.POST['fname']
            lname = request.POST['lname']
            prof=request.POST['prof']
            age=request.POST['age']
            live=request.POST['live']
            gender=request.POST['gender']
            about1=request.POST['about']

            about = About.objects.last()
            about.fname = fname
            about.lname = lname
            about.prof = prof
            about.about = about1
            about.age = age
            about.live= live
            about.gender = gender
            
            about.save()
            return HttpResponseRedirect(reverse('index'))