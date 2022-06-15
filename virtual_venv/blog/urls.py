from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('achievements/', views.achievements, name='achievements'),
    path('getachievements/', views.getachievements, name='getachievements'),
    path('gethobbies/', views.gethobbies, name='gethobbies'),
    path('getachievements/getconferences/', views.getconferences, name='getconferences')
]