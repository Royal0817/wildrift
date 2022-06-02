from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('champions/', views.ChampionList.as_view(), name='champions'),
    path('artist/<int:pk>/', views.ChampionDetail.as_view(), name="champ_detail"),

]