from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.company_info.urls')), 
    path('events/', include('apps.events.urls')),
    path('organizations/', include('apps.organizations.urls')),
    path('vacancy/', include('apps.vacancy.urls')),
    path('vacncy_description/', include('apps.vacancy.urls')),
    path('videos/', include('apps.videos.urls')),
    path('users/', include('apps.users.urls')),
    path('login/', include('rest_framework.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)