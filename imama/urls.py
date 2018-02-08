from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pacientes, name='pacientes'),
    url(r'^paciente/(?P<pk>\d+)/$', views.paciente_detalhe, name='paciente_detalhe'),
    url(r'^paciente/adicionar', views.nova_paciente, name='nova_paciente'),
    url(r'^paciente/(?P<pk>\d+)/editar/$', views.editar_paciente, name='editar_paciente'),


]

    #url(r'^$', views.entrevista, name='entrevista'),
    #url(r'^$', view.amigo_rosa, name='amigo_rosa')
