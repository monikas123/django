
from django.urls import path
from . import views
urlpatterns = [
    path('', views.subscribe, name = 'subscribe'),
    path('cripsy/', views.cripsy, name = 'cripsy'),
    path('exampleform/', views.exapleForm, name = 'exapleForm'),
    path('address/', views.addressform, name = 'address')
]