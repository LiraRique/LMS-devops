'''
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    #PAGINAS DAS HOMES
    path('', index),
    path('contato/', contato),
    path('graduacao/', graduacao),
    path('login/', login),
    path('noticia/', noticia),
    path('ADS/', ads),
    path('WebDesigner/', WebDesigner),
    path('BancoDeDados/', BancoDeDados),

#CURSOS
    path('graduacao/ADS/', ads),
    path('graduacao/SI/', si),
    path('graduacao/WebDesigner/', WebDesigner),
    path('graduacao/JogosDigitais/', JogosDigitais),
    path('graduacao/BancoDeDados/', BancoDeDados),
    path('graduacao/ProducaoMultimidia/', ProducaoMultimidia),

#DASHBOARDS ALUNO
    path('login/dashboardAluno/', DashAluno),
    path('login/dashboardAluno/calendario_geral/', calendario_aluno),
    path('login/dashboardAluno/atividades_entregue/', atividades_entregue_aluno),
    path('login/dashboardAluno/ouvidoria/', ouvidoria_aluno),
    path('login/dashboardAluno/financeiro/', financeiro_aluno),
    path('login/dashboardAluno/conta/', conta_aluno),


    path('login/dashboardProf/', DashProf),
    path('login/dashboardProf/calendario_prof/', calendario_prof),
    path('login/dashboardProf/planejamento_aula/', planejamento_aula),
    path('login/dashboardProf/ouvidoria_prof/', ouvidoria_prof),
    path('login/dashboardProf/corrigir_atividade_prof/', corrigir_atividade_prof),
    path('login/dashboardProf/conta_prof/', conta_prof),

    path('admin/', admin.site.urls),
]
'''

"""
Definition of urls for django_get_started.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.index', name='home'),
    url(r'^contato$', 'app.views.contato', name='contato'),
    url(r'^graduacao', 'app.views.graduacao', name='graduacao'),
    url(r'^cadastro_cursos', 'app.views.cadastro_cursos', name='cadastro_cursos'),
    url(r'^Curso-ADS', 'app.views.ads', name='Curso-ADS'),


        
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
