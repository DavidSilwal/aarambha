"""aarambha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from webapp import views

urlpatterns = [
    url(r'^$', views.home,name='home',),
    url(r'^whoweare', views.whoweare,name='whoweare',),
    url(r'^whatwedo', views.whatwedo,name='whatwedo',),
    url(r'^aboutus$', views.aboutus,name='aboutus',),
    url(r'^blog', views.blog,name='blog',),
    url(r'^about$', views.about,name='about',),
    url(r'^faq', views.faq,name='faq',),
    url(r'^contact', views.contact,name='contact',),
    url(r'^support', views.support,name='support',),
    url(r'^event', views.event,name='event',),
    url(r'^work$', views.work,name='work',),
    url(r'^working$', views.working, name='working',),
    url(r'^admin/', admin.site.urls),
    
]
