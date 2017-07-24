from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listado, name='listado'),
#    url(r'^individuo/(?P<pk>\d+)$', views.individuo, name='individuo'),
    url(r'^dato/nuevo/$', views.entrada, name='entrada'),
    url(r'^resultado/$', views.resultado, name='resultado'),
]
