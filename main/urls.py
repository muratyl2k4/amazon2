from django.urls import path
from .views import home , pl , kargotakip , muhasebe
urlpatterns = [
    path("" , home , name="home"),
    path("home" , home),
    path("kargotakip" , kargotakip),
    path("pl" , pl),
    path("muhasebe" , muhasebe),
]