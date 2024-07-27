from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),  # defining path to home page of the blog
    path('about/', views.about, name='blog-about'),
]
