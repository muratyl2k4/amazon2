from django.urls import path
from .views import home , pl , muhasebe , muhasebe_update
urlpatterns = [
    path("" , home , name="home"),
    path("home" , home),
    path("pl" , pl),
    path("muhasebe" , muhasebe),
    path("muhasebe/<int:id>" , muhasebe_update),
]