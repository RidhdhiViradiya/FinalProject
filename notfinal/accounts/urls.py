
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="RegisterPage"),
    path('login/', views.login, name="LoginPage"),
]
