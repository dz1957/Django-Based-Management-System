"""
URL configuration for phone_number_management project.

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
from web.views import account
from web.views import admin

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("login/", account.login),
    path("img/code/", account.img_code),
    path("home/", account.home),
    path("layout/", account.layout),
    path("logout/", account.logout),
    path("admin/list/", admin.admin_list),
    path("admin/add/", admin.admin_add),
    path("admin/add/depart/",admin.admin_add_depart)
]
