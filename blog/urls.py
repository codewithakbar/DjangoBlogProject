from django.urls import path
from .views import BlogListView, BlogDetialView, BlogCreateView

urlpatterns = [
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetialView.as_view(), name='post_detail'),
]

