"""ProyectoTapizados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from AplicacionTapizados import views

urlpatterns = [
    #path('admin/', admin.site.urls)
    path('', views.Vlogin , name='inicio'),
    path('AdminLog', views.VloginAdmin, name="loginAd"),
    path('VUsuario', views.VistaUsuario, name="ViUsu"),
    path('RegistroU', views.RegistroUsuario, name="RUsuario"),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('login/', views.login_view, name='login'),
    path('VAdmin', views.VistaAdmin, name="ViAdm"),
]

    

