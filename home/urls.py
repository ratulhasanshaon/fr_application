from django.urls import path
from django.urls import re_path
from django.contrib import admin
from home import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('addFace/', views.addFace),
    re_path(r'^welcome/(?P<face_id>\d+)/$', views.welcome),
]
