from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index,name='index'),
    path('posts/<str:pk>',views.post,name='post'),
    path('weather',views.weather,name='weather'),
    path('',views.home,name='home'),
    # path('<str:room>/',views.room,name='room'),
    path('checkview',views.checkview,name='checkview')
]
