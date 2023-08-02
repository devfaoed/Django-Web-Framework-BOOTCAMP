from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('dishes/<str:dish>', views.menuitems, name="menuitems"),
]