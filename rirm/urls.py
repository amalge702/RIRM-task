from django.urls import path

from . import views

urlpatterns=[
 path('', views.index, name='index'),
 path('register/', views.handleregister, name='register page'),
 path('search/', views.search, name='search page'),

]