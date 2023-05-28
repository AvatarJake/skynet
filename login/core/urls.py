
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/',include('djoser.urls')),
    path('login/',include('djoser.urls.jwt')),
    path('login/',include('djoser.social.urls')),

    path('api/users',include('apps.user.urls')),
    path('api/profiles',include('apps.profile.urls')),
    
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
