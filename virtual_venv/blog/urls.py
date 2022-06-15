from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('achievements/', views.achievements, name='achievements'),
    path('getachievements/', views.getachievements, name='getachievements'),
    path('gethobbies/', views.gethobbies, name='gethobbies'),
    path('getconferences/', views.getconferences, name='getconferences')
]