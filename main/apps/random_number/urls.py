from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^rand$', views.index),
	url(r'^random_number/generate$', views.generate)
]