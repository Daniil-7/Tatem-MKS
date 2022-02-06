from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
	path('menu/', views.index, name='index'),
	path('menu/news/', views.news, name='news'),
	path('menu/track/', views.track, name='track'),
	path('menu/imageday/', views.imageday, name='imageday')
]
