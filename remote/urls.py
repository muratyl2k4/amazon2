from django.urls import path 
from .views import fbaHomePage , fbaMarketPage, fbaMarketPoolPage
urlpatterns = [
    path("fba" , fbaHomePage),
    path("fba/<str:country>" , fbaMarketPage),
    path("fba/<str:country>/pool" , fbaMarketPoolPage)
]
