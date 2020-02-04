from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('register/registerUser', views.registerUser, name="UserRegister"),
    path('register/', views.register, name="RegisterPage"),
    path('login/', views.login, name="LoginPage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
