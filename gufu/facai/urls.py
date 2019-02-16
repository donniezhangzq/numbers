from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^result$', views.result, name='result'),
	url(r'^getdata$', views.getdata, name='getdata'),
]
