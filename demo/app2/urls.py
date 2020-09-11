from django.conf.urls import url
from django.urls import path
from .import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('user', views.user, name="user"),
    path('userList', views.userList, name="userList"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update"),

]