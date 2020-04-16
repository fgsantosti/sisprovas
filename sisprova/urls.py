from django.conf.urls import include, url
from . import views

urlpatterns = [
	#url(r'^$', views.disciplina_list),
	url(r'^$', views.index, name='index'),
	url(r'^$', views.sisprova, name='sisprova'),
	url(r'^login-in/$', views.login_in, name='login_in'),
	url(r'^login/$', views.login_view, name='login_view'),
	url(r'^login-professor/$', views.login_professor, name='login_professor'),
	url(r'^perfil/$', views.perfil, name='perfil'),
	url(r'^logout/$', views.logout_view, name='logout_view'),
	url(r'^contato/$', views.contato, name='contato'),
	url(r'^sobre/$', views.sobre, name='sobre'),
	url(r'^perguntas-objetivas/$', views.perguntas_objetivas_list, name="perguntas_objetivas_list"),
	url(r'^perguntas-list/$', views.perguntas_list, name="perguntas_list"),
	url(r'^prova-selecionada/$', views.prova_selecionada, name="prova_selecionada"),
	url(r'^prova-selecionada-paginacao/$', views.prova_selecionada_paginacao, name="prova_selecionada_paginacao"),
	url(r'^respostas-selecionadas/$', views.respostas_selecionadas, name="respostas_selecionadas"),
	#detalhar questao por id
	url(r'^detalhar/(?P<perguntas_detalhe_id>[0-9]+)/$', views.detalhe, name="detalhar"),
	#detalhar as questoes selecionadas pelo professor para a turma
	url(r'^prova-turma/(?P<prova_selecionada_id>[0-9]+)/$', views.ir_prova, name="ir_prova"),
	#rota para buscar por assunto
	url(r'^buscar_assunto/$', views.buscar_assunto, name="buscar_assunto"),
	#url(r'^sisprova/perguntas-list/$', views.perguntas_list),
	#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	#url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
