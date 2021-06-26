# -*- coding: utf-8 -*-

from django.urls import path
from .import views 

urlpatterns=[
               path('index1',views.index1,name='index1'),
               path('register',views.register,name='register'),
               path('login',views.login,name='login'),
               path('packages',views.packages,name='packages'),
               path('about',views.about,name='about'),
               path('resetpassword',views.resetpassword,name='resetpassword'),
               path('contact',views.contact,name='contact'),
               path('prediction',views.prediction,name='prediction'),
               path('result',views.result,name='result'),
               path('logout', views.logout,name='logout')
              
               
             
           ]