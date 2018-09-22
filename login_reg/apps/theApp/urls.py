from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^theApp/create$', views.create),
    url(r'^theApp/logIn$', views.logIn),
    url(r'^theApp/new$', views.new),
    url(r'^theApp/success$', views.success)
]