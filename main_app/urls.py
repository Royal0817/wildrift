from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('champions/', views.ChampionList.as_view(), name='champions')
]