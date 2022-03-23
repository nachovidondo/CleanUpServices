
from django.urls import path
from .views import index , services, contact, automatic, portfolio, places

urlpatterns = [
    path('', index, name ="index"),
    path('services/', services, name ="services"),
    path('contact/', contact ,name ="contact"),
    path('automatic/', automatic, name="automatic"),
    path('portfolio/', portfolio, name="portfolio"),
    path('places/', places, name="places"),
]