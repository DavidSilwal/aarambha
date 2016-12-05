
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from webapp.models import *

def home(request):
    return render(request,'webapp/index.html',{
        'title':'Home',
        'year':'2016',
        'blog':Blog.objects.all()[:5],
        'event':Event.objects.all()[:5],
        'work':Work.objects.all()[:5],
    })
    
def whoweare(request):
    return render(request,'webapp/whoweare.html',{
        'title':'Who we are',
        
    })

def whatwedo(request):
    return render(request,'webapp/whatwedo.html',{
        'title':'What we do',
        
    })
    
def about(request):
    return render(request,'webapp/about.html',{
        'title':'About',
    }
    )
    


def blog(request):
    return render(request,'webapp/blog.html', {
        'blog':Blog.objects.all(),
        'title':'Blog Feed',
    })

def work(request):
    return render(request,'webapp/work.html', {
        'work':Work.objects.all(),
        'title':'Our Works',
    })
    
    
def working(request):
    return render(request,'webapp/working.html',)

def event(request):
    return render(request,'webapp/event.html', {
        'event':Event.objects.all(),
        'title':'Our Events',
    })
        
def aboutus(request):
    return render(request,'webapp/aboutus.html',{
    'title':'About Us',
    'member':Member.objects.all(),
    },)

def faq(request):
    return render(request,'webapp/faq.html',{
    'title':'FAQ',
    },)

def contact(request):
    return render(request,'webapp/contact.html',{
        'title':'Contact',
    },)
    
def support(request):
    return render(request,'webapp/support.html',{
    'title':'Support',
    },)

    

