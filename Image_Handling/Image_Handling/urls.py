from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from Image_Handling import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^myapp/', include('myapp.urls', namespace='myapp')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)