from django.urls import path
from .views import (
    PostDeleteView,
    PostDetailView, 
    PostListView, 
    PostCreateView,
    PostUpdateView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # defining path to home page of the blog
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),  
    path('post/new/', PostCreateView.as_view(), name='post-create'),  
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  
    path('about/', views.about, name='blog-about'),
]
