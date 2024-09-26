from django.contrib import admin
from django.urls import path,include
from Home import views

urlpatterns = [
    path("",views.index,name='Home'),
    path("about",views.about,name = 'about'),
    path("projects",views.projects,name = 'projects'),
    path("contactus",views.contactus,name = 'contactus'),
    path("login",views.loginUser,name="login"),
    path("logout",views.logoutUser,name="logout"),
    path("profile",views.profile,name="profile"),
    path("signup",views.signup,name="signup"),
    path("javascript",views.javascript,name="javascript"),
]
