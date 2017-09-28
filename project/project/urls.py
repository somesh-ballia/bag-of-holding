from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout


base_urlpatterns = [
    url(r'^', include('boh.urls', namespace='boh')),
    url(r'^api/', include('boh_api.urls', namespace='boh_api')),
    url(r'^accounts/logout/$', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
]

# Apply URL_PREFIX setting to all urls
if settings.URL_PREFIX:
    urlpatterns = [
        url(r'^' + settings.URL_PREFIX, include(base_urlpatterns)),
    ]
else:
    urlpatterns = base_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
