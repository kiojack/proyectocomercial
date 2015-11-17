from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.reservacion_list),
    url(r'^hab$', views.habitacion_list),
 ]