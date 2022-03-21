
from django.urls import path
from .views import index , services

urlpatterns = [
    path('', index, name ="index"),
    path('services/', services, name ="services")
]