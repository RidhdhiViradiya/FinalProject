from . import views
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', views.index, name="MainHome"),
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('payingGuest/', include('payingGuest.urls')),
]
