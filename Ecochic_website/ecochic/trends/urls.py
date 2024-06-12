from django.urls import path
from . import views

app_name = "trends"

urlpatterns = [
    path('', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('wardrobe/', views.wardrobe, name='wardrobe'),
    path('milestones/', views.milestones, name='milestones'),
    path('trending/', views.trending, name='trending'),
]
