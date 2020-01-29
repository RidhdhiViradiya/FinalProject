
from django.urls import path
from . import views

urlpatterns = [
    path('register/registerUser', views.registerUser, name="UserRegister"),
    path('register/', views.register, name="RegisterPage"),
    path('login/', views.login, name="LoginPage"),
]
