from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^myapp/', include('myapp.urls', namespace="myapp")),
    url(r'^admin/', include(admin.site.urls)),
)
