from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<str:pk>',views.post,name='post'),
    path('weather',views.weather,name='weather'),
    path('home',views.home,name='home')
    # path('notification')
]
