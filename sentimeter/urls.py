from django.conf.urls import url
from . import views
from .views import userinput

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^input/$', views.analyse, name='input'),
]