"""DayPlanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home.as_view(),name="home"),
    # path('about/', views.About,name="about"),
    
    path('addtask/', views.CreateTask,name="addtask"),
    path('addtask/<int:pk>/', views.UpdateTask, name="task_update"),
    path('addtask/<int:pk>/delete', views.DeleteTask, name="deletetask"),
    
    path('addtask/deletecomment', views.DeleteComment, name="delete_comment"),
    path('searchTask/',views.SearchTask, name="search_task"),
    path('accounts/signup/', views.Signup, name="signup"),
]
