from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.reservacion_list),
    url(r'^hab$', views.habitacion_list),
    url(r'^dethab/(?P<pk>[0-9]+)/$', views.detalle_habitacion),
    url(r'^detreservacion/(?P<pk>[0-9]+)/$', views.detalle_reservacion),
    url(r'^hab/nuevo/$', views.nueva_hab, name='nuevo_hab'),
    url(r'^hab/editar/(?P<pk>[0-9]+)$', views.editar_hab, name='editar_hab'),
    url(r'^reservar/editar/(?P<pk>[0-9]+)$', views.editar_reserva, name='editar_reserva'),
 ]