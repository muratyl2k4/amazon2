from django.urls import path 
from .views import upload

urlpatterns = [
    path("uploadfile" , upload)
]
