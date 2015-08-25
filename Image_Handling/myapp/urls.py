from django.conf.urls import patterns, include, url
from myapp import views
from myapp import forms

urlpatterns = [
               url(r'^$', views.sign_up, name='signup'),
               url(r'^signup', views.sign_up, name='signup'),
               url(r'^login', views.login_view, name='login'),
               url(r'^profile', views.profile, name='profile'),
               url(r'^uploadpicture', views.upload_picture, name='uploadpicture'),
               url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/myapp/login'})
               ]