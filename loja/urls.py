"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from . import views

app_name = "loja"

urlpatterns = [
path('login/', views.login),
path('logout/', views.logout),\
path('home/', views.home),\
path('addresses/', views.address_list, name="address_list"),\
path('addresses/create/', views.address_create, name="address_create"),\
path('addresses/<int:id>/update/', views.address_update, name="address_update"),
path('addresses/<int:id>/delete', views.address_delete, name="address_delete")
]