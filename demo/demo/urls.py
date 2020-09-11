"""demo URL Configuration

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
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from webapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('calc/', include('calc.urls')),
    path('app2/', include('app2.urls')),
    path('travelo/', include('travelo.urls')),
    path('app3/', include('app3.urls')),
    path('subscribe/', include('subscribe.urls')),
    path('api/', include('api.urls')),
    path('employee/', views.employeeList.as_view()),
    path('contact/', include('myapi.urls')),

]
