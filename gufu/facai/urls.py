from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^version2$', views.version2, name='version2'),
	url(r'^result$', views.result, name='result'),
	url(r'^result_version2$', views.result_version2, name='result_version2'),
	url(r'^getdata$', views.getdata, name='getdata'),
]
