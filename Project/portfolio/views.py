from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Page1
from .models import About
from .models import Skill
from .models import Skill1
from .models import Education
from .models import Exp


# Create your views here.



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
    skill=Skill.objects.all()
    skill1=Skill1.objects.all()
    edu = Education.objects.all()
    exp = Exp.objects.all()
    portfolio = Portfolio.objects.all()
    footer=Footer.objects.last
    template = loader.get_template('index.html')
    context = {
        'values': value,
        'about':about,
        'skill': skill,
        'skill1': skill1,
        'edu':edu,
        'exp':exp,
        'portfolio':portfolio,
        'footer':footer
       
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









#Skill Page
def skill_add(request):
        template = loader.get_template('skill_add.html')
        return HttpResponse(template.render({}, request))

# def skill_all(request):
#         template = loader.get_template('skill_all.html')
#         return HttpResponse(template.render({}, request))



def skill_add_do(request):
            name = request.POST['name']
            per = request.POST['per']
          
            skill = Skill(name = name,
                          per=per
            )
            skill.save()
            return HttpResponseRedirect(reverse('skill_all'))

def skill_add_do1(request):
            name = request.POST['name1']
            per = request.POST['per1']
          
            skill = Skill1(name = name,
                          per=per
            )
            skill.save()
            return HttpResponseRedirect(reverse('skill_all'))

def skill_all(request):
    skill = Skill.objects.all().values()
    skill1 = Skill1.objects.all().values()
    template = loader.get_template('skill_all.html')
    context = {
        'skill': skill,
        'skill1': skill1,
    }
    return HttpResponse(template.render(context, request))

def skill_delete(request, id):
            member = Skill.objects.get(id=id)
            member.delete()
            return HttpResponseRedirect(reverse('skill_all'))

def skill_delete1(request, id):
            member = Skill1.objects.get(id=id)
            member.delete()
            return HttpResponseRedirect(reverse('skill_all'))







#education


def edu_add(request):
        template = loader.get_template('edu_add.html')
        return HttpResponse(template.render({}, request))


def edu_add_do(request):
            year = request.POST['year']
            degree = request.POST['degree']
            uni = request.POST['uni']
            detail = request.POST['detail']
          
            edu = Education(
                    year = year,
            degree = degree,
            uni = uni,
            detail = detail
            )
            edu.save()
            return HttpResponseRedirect(reverse('edu_all'))

def edu_all(request):
    edu = Education.objects.all().values()
    template = loader.get_template('edu_all.html')
    context = {
        'edu': edu,
    }
    return HttpResponse(template.render(context, request))


def edu_update(request, id):
            edu = Education.objects.get(id=id)
            template = loader.get_template('edu_update.html')
            context = {
                'edu': edu,
            }
            return HttpResponse(template.render(context, request)) 

def edu_update_do(request, id):
            year = request.POST['year']
            degree = request.POST['degree']
            uni = request.POST['uni']
            detail = request.POST['detail']

            edu = Education.objects.get(id=id)
            edu.year = year
            edu.degree = degree
            edu.uni = uni
            edu.detail = detail
            
            edu.save()
            return HttpResponseRedirect(reverse('edu_all'))
        
def edu_delete(request, id):
            edu = Education.objects.get(id=id)
            edu.delete()
            return HttpResponseRedirect(reverse('edu_all'))        


#Experience

#education


def exp_add(request):
        template = loader.get_template('exp_add.html')
        return HttpResponse(template.render({}, request))


def exp_add_do(request):
            year = request.POST['year']
            degree = request.POST['degree']
            uni = request.POST['uni']
            detail = request.POST['detail']
          
            exp = Exp(
                    year = year,
            degree = degree,
            uni = uni,
            detail = detail
            )
            exp.save()
            return HttpResponseRedirect(reverse('index'))

def exp_all(request):
    exp = Exp.objects.all().values()
    template = loader.get_template('exp_all.html')
    context = {
        'exp': exp,
    }
    return HttpResponse(template.render(context, request))


def exp_update(request, id):
            exp = Exp.objects.get(id=id)
            template = loader.get_template('exp_update.html')
            context = {
                'exp': exp,
            }
            return HttpResponse(template.render(context, request)) 

def exp_update_do(request, id):
            year = request.POST['year']
            degree = request.POST['degree']
            uni = request.POST['uni']
            detail = request.POST['detail']

            exp = Exp.objects.get(id=id)
            exp.year = year
            exp.degree = degree
            exp.uni = uni
            exp.detail = detail
            
            exp.save()
            return HttpResponseRedirect(reverse('exp_all'))
        
def exp_delete(request, id):
            exp = Exp.objects.get(id=id)
            exp.delete()
            return HttpResponseRedirect(reverse('exp_all'))      










from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


def portfolio_add(request):
 
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PortfolioForm()
    return render(request, 'portfolio.html', {'form': form})
 

def success(request):
    return HttpResponse('successfully uploaded')

def portfolio_all(request):
 
    if request.method == 'GET':
 
        # getting all the objects of hotel.
        portfolio = Portfolio.objects.all()
    
        template = loader.get_template('portfolio_all.html')
        context = {
            'portfolio': portfolio
        }
        return HttpResponse(template.render(context, request))

    
def portfolio_delete(request, id):
            portfolio = Portfolio.objects.get(id=id)
            portfolio.delete()   
            return HttpResponse('successfully Deleted') 

def portfolio_detail(request, id):
            detail = Portfolio.objects.get(id=id)
              
            template = loader.get_template('portfolio_detail.html')
            context = {
                'detail': detail
            }
            return HttpResponse(template.render(context, request)) 

    

    # Footer

def footer_add(request):
        template = loader.get_template('footer_add.html')
        return HttpResponse(template.render({}, request))

def footer_add_do(request):
            name = request.POST['name']
            addr = request.POST['addr']
            insta = request.POST['insta']
            linkedin = request.POST['linkedin']
            twitter = request.POST['twitter']
            facebook = request.POST['facebook']
            youtube = request.POST['youtube']
            email = request.POST['email']
            phone=request.POST['phone']
            
          
            footer = Footer(
            name = name,
            addr = addr,
            insta =insta,
            linkedin = linkedin,
            twitter = twitter,
            facebook =facebook,
            youtube = youtube,
            email = email,
            phone=phone,
            
            )
            footer.save()
            return HttpResponseRedirect(reverse('index'))


def footer_update(request):
        footer = Footer.objects.last
        template = loader.get_template('footer_update.html')
        context = {
            'footer': footer,
        }
        return HttpResponse(template.render(context, request))

def footer_update_do(request):
            name = request.POST['name']
            addr = request.POST['addr']
            insta = request.POST['insta']
            linkedin = request.POST['linkedin']
            twitter = request.POST['twitter']
            facebook = request.POST['facebook']
            youtube = request.POST['youtube']
            email = request.POST['email']
            phone=request.POST['phone']

            footer = Footer.objects.last()
            footer = Footer(
            name = name,
            addr = addr,
            insta =insta,
            linkedin = linkedin,
            twitter = twitter,
            facebook =facebook,
            youtube = youtube,
            email = email,
            phone=phone,
            
            )
            
            
            footer.save()
            return HttpResponseRedirect(reverse('index'))    