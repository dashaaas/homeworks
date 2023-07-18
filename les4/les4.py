views.py:
from django.shortcuts import render
from django.http import HttpResponse

def lesson(request):
    return HttpResponse('Домашка по 4 занятию')


app_lesson_4\urls.py:
from django.urls import path
from .views import lesson

urlpatterns = [
    path('', lesson)
]


advertisements\urls.py:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_advertisements.urls')),
    path('lesson_4', include('app_lesson_4.urls')),
]


setting.py --> INSTALLED_APPS:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_advertisements',
    'app_lesson_4',
]


