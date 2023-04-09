from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('account/', include('register.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
]

if settings.DEBUG:
    urlpatterns += (
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
