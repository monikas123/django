from django.urls import path
from .import views


urlpatterns=[
path('createpost/', views.createpost, name='createpost'),

path('register/', views.register, name='register'),




]