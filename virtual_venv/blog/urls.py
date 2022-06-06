from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('achievements/', views.achievements, name='achievements'),
    path('achievements/getachievements/', views.getachievements, name='getachievements')
]