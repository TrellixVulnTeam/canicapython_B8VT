"""canica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from nino import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('noticias/', views.noticias, name='noticias'),
    path('programas/', views.programas, name='programas'),
    path('nino/', include('nino.urls')),
    path('admin/', admin.site.urls),
]