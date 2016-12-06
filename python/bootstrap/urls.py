from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^external/', include('external.urls')),
    url(r'^dev/', include('dev.urls')),
]
