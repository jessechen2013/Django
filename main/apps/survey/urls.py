from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^survey$', views.index),
	url(r'^survey/process$', views.process),
	url(r'^result$', views.view_result)
]