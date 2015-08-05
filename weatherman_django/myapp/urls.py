from django.conf.urls import include, url
from django.contrib import admin
from myapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^report1/$', views.report1, name='report1'),
    url(r'^report2/$', views.report2, name='report2'),

    url(r'^admin/', include(admin.site.urls)),
]

