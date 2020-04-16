# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Disciplina, Pergunta_Objetiva, Prova_Selecionada, Resposta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
#redireciona para página de login
#direciona o usuario para pagina index
def login_in(request):
	return render(request, 'sisprova/login.html')

def sisprova(request):
	return render(request, 'sisprova/index.html')

def perfil(request):
	return render(request, 'sisprova/perfil.html')

def login_view(request):
	provas = Prova_Selecionada.objects.all()
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(request, username=username, password=password)
	#pegando o nome da turma
	for g in user.groups.all():
	    grupo = g.name
	#pega qual turma o aluno esta
	grupo_id = Group.objects.get(name=grupo)
	#seleciona as questoes que estao relacionadas as turma do aluno
	provas_selecionadas = Prova_Selecionada.objects.filter(grupo=grupo_id)
	quant_provas = len(provas_selecionadas)

	request.session['name'] = user.id
	if user is not None:
		if user.is_active:
			auth.login(request, user)
			return render(request, 'sisprova/perfil.html', {'user':user, 'grupo':grupo, 
				'provas':provas, 'quant_provas':quant_provas, 'grupo_id':grupo_id,
				'provas_selecionadas':provas_selecionadas})
	else:
		return HttpResponseNotFound('<h2>Page not found</h2>')
    
def logout_view(request):
	logout(request)
	return render(request, 'sisprova/login.html')

#direciona o usuario para pagina index
def index(request):
	return render(request, 'sisprova/index.html')
#direciona o usuario para pagina contato
def contato(request):
	return render(request, 'sisprova/contato.html')
#direciona o usuario para pagina sobre 
def sobre(request):
	return render(request, 'sisprova/sobre.html')

#direciona o usuario para pagina index
def login_professor(request):
	return render(request, 'sisprova/login_professor.html')

#Lista todas as questoes objetivas contidas no banco de dados
def perguntas_objetivas_list(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(request, username=username, password=password)
	if user is not None:
		#verifica superuser
		if user.is_superuser:
			auth.login(request, user)
			perguntas_objetiva = Pergunta_Objetiva.objects.all().order_by('data')
			disciplinas = Disciplina.objects.all().order_by('nome')
			#lista todas as turmas inseridas no bd
			turmas = Group.objects.all().order_by('name')
			return render(request, 'sisprova/perguntas_objetivas_list.html', 
				{'perguntas_objetiva': perguntas_objetiva, 'disciplinas':disciplinas,
				'turmas':turmas})
	else:
		return HttpResponseNotFound('<h2>Page not found</h2>')

#Mostra a pagina para listrar as perguntas
def perguntas_list(request):
	return render(request, 'sisprova/perguntas_list.html')

#Detalha a pergunta selecionada
def detalhe(request, perguntas_detalhe_id):
	perguntas_detalhe = get_object_or_404(Pergunta_Objetiva,pk=perguntas_detalhe_id)
 	return render(request, 'sisprova/perguntas_detalhe.html', 
 		{'perguntas_detalhe': perguntas_detalhe})

#realiza uma busca por disciplina
def buscar_assunto(request):
	disciplinas = Disciplina.objects.all().order_by('nome')
	perguntas_objetiva = Pergunta_Objetiva.objects.filter(disciplina=request.POST['disciplina'])
	#lista todas as turmas inseridas no bd
	turmas = Group.objects.all().order_by('name')
	return render(request, 'sisprova/perguntas_objetivas_list.html', 
		{'perguntas_objetiva': perguntas_objetiva, 'disciplinas':disciplinas, 
		'turmas':turmas})

def prova_selecionada(request):
	perguntas_objetiva = Pergunta_Objetiva.objects.all()		
	if request.method == 'POST':
		#selecionada apenas as questoes selecionadas
		questoes=request.POST.getlist('questoes')

		grupo_id = Group.objects.get(name=request.POST['disciplina'])
		#gravando a prova selecionada para a turma x
		prova_selecionada = Prova_Selecionada.objects.create(questoes=request.POST.getlist('questoes'),
			nome_prova=request.POST['nomeprova'], data=timezone.now(), grupo=grupo_id)
		prova_selecionada.save()
	#pega do banco de dados apenas as questoes selecionadas
	questoes_selecionadas = Pergunta_Objetiva.objects.filter(pk__in=questoes)
	#questoes_respostas = Pergunta_Objetiva.objects.filter(pk__in=questoes)

	return render(request, 'sisprova/prova_selecionada.html',{'questoes_selecionadas':questoes_selecionadas, 
		'prova_selecionada':prova_selecionada, 'questoes':questoes})

#Funcao que pega o id da prova selecionada e leva o aluno para prova
def ir_prova(request, prova_selecionada_id):
	prova_detalhe = Prova_Selecionada.objects.get(pk=prova_selecionada_id)
	
	a = eval(prova_detalhe.questoes)
	b = [str(x) for x in a]
	c = [int(x) for x in b]

	prova_questoes = Pergunta_Objetiva.objects.filter(pk__in=c)
 	
 	return render(request, 'sisprova/prova_detalhe.html', 
 		{'prova_questoes':prova_questoes, 'prova_selecionada_id':prova_selecionada_id})

def respostas_selecionadas(request):
	prova_selecionada = Prova_Selecionada.objects.all()
	perguntas_objetiva = Pergunta_Objetiva.objects.all()
	respostas = request.POST.getlist('resp')
	provaselecionada = request.POST['provaselecionada']

	if request.method == 'POST':
		respostas = request.POST.getlist('resp')
		#questoes = request.POST['questoes']
		#idprova=prova_selecionada.get(id=request.POST['provaselecionada'])
		#respostas_selecionada = Resposta.objects.create(prova_selecionada=request.POST['provaselecionada'], 
			#respostas=respostas, nome_aluno=request.POST['nomealuno'], data=timezone.now())
		#respostas_selecionada.save()
		questoes = Prova_Selecionada.objects.get(pk=request.POST['provaselecionada'])
	a =  eval(questoes.questoes)
	b = [str(x) for x in a]
	c = [int(x) for x in b]
	respostas_corretas = Pergunta_Objetiva.objects.filter(pk__in=c)
	#Verificando quantas questoes o aluno acertou
	indice = 0
	quant_corretas = 0

	while indice<len(respostas_corretas):
	 	temp = respostas_corretas[indice]
	 	temp_correta = temp.alternativa_correta
		if respostas[indice] == temp_correta:
		 	quant_corretas = quant_corretas + 1
	 	indice = indice + 1 

	#verificando a porcetagem da prova
	quant_questoes = len(respostas_corretas)
	valor_porcetagem =  float((100*quant_corretas)/quant_questoes)

	return render(request, 'sisprova/nota_aluno.html',{'respostas':respostas, 'provaselecionada':provaselecionada, 
		'questoes':questoes, 'respostas_corretas':respostas_corretas, 'valor_porcetagem':valor_porcetagem, 'quant_corretas':quant_corretas})

def prova_selecionada_paginacao(request):
	perguntas_objetiva = Pergunta_Objetiva.objects.all()
	paginator = Paginator(perguntas_objetiva, 1) # Show 1 question per page

	page = request.GET.get('page')
	try:
		perguntas_objetiva = paginator.page(page)
	except PageNotAnInteger:
		perguntas_objetiva = paginator.page(1)
	except EmptyPage:
		perguntas_objetiva = paginator.page(paginator.num_pages)

	return render(request, 'sisprova/list_paginacao.html', {'perguntas_objetiva':perguntas_objetiva})

#TODA PROVA SELECIONADA TEM UM ID, ESSE ID DEVE ESTÁ NA RESPOSTAS SELECIONADAS
def nota_aluno(id_prova, respostas_selecionadas):
	return render(request, 'sisprova/nota_aluno.html', {'id-prova':id_prova})

