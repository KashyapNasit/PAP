"""PAP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url
from login import views as core_views
from administrator import views as admin_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home),
    path('home/', core_views.home, name='home'),
    url(r'^login/', include('login.urls')),
    path('professors/', include('professor.urls')),
    path('administrator/', include('administrator.urls')),
    url('group/',core_views.group),
]
