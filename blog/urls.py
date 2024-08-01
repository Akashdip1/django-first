from django.urls import path
from .views import (
    PostDetailView, 
    PostListView, 
    PostCreateView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # defining path to home page of the blog
    path('post/int:<pk>', PostDetailView.as_view(), name='post-detail'),  
    path('post/new/', PostCreateView.as_view(), name='post-create'),  
    path('about/', views.about, name='blog-about'),
]
