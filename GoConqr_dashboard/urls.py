from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
path('',views.index,name='index'),
path('login',views.login, name='login'),
path('dashboard',views.dashboard,name='dashboard'),
path('logout',views.logout,name='logout'),
path('profill',views.profill,name='profill'),
path('contact',views.contact,name='contact'),
path('about',views.about,name='about')
]