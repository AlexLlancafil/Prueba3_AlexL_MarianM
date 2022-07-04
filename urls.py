"""prueba3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from re import template
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Registro , CustomLoginView
from django.conf import settings
from django.conf.urls.static import static
from .forms import loginForm 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('Compras/', views.Compras),
    path('Seguimiento/', views.Seguimiento),
    path('eliminarProducto/<id>', views.eliminarProducto),
    path('agregarPelicula/', views.agregarPelicula),
    path('login/', views.login),
    path('Donacion/', views.Donacion),
    path('registro/', Registro.as_view(), name='registro'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='static/login.html', authetication_form=loginForm), name='login'),
    path('Contacto/', auth_views.LogoutView.as_view( template_name='logut.htmol'), name='static/Contacto.html'),

]
