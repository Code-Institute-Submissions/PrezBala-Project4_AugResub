from django.urls import path, include
from .views import (
    home, detail, posts)


urlpatterns = [
    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    path('tinymce/', include('tinymce.urls')),
]
