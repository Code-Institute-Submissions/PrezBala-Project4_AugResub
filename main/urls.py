from django.urls import path, include
from .views import (
    home, detail, posts, create_post, latest_posts,
    search_result,)
from . import views


urlpatterns = [
    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    path("create_post", create_post, name="create_post"),
    path("latest_posts", latest_posts, name="latest_posts"),
    path("search", search_result, name="search_result"),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('edit_post/<int:pk>/', views.EditPost.as_view(), name='edit_post'),
    path(
        'delete_post/<int:pk>/',
        views.DeletePost.as_view(),
        name='delete_post'
    ),
    path('approve_post/<int:pk>/', views.approve_post, name='approve_post'),
]
