from django.urls import path
from .views import home , pl , kargotakip , muhasebe , muhasebe_update
urlpatterns = [
    path("" , home , name="home"),
    path("home" , home),
    path("kargotakip" , kargotakip),
    path("pl" , pl),
    path("muhasebe" , muhasebe),
    path("muhasebe/<int:id>" , muhasebe_update),
]