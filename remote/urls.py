from django.urls import path 
from .views import fbaHomePage , fbaMarketPage
urlpatterns = [
    path("fba" , fbaHomePage),
    path("fba/<str:country>" , fbaMarketPage)
]
