"""
URL configuration for todolist_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
####### NEW #######
from tasks import views  # Import the views module from the tasks app
####### NEW #######

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

####### NEW #######
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:pk>/', views.mark_completed, name='mark_completed'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]
####### NEW #######
