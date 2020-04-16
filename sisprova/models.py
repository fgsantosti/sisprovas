from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField


class Disciplina(models.Model):
	"""docstring for Disciplina"""
	nome 	= models.CharField(max_length = 200)
	descricao = models.TextField()
	def __str__(self):
		return self.nome.encode('utf8')
		
class Pergunta_Objetiva(models.Model):
	"""docstring for Pergunta"""
	author = models.ForeignKey('auth.User')
	disciplina = models.ForeignKey(Disciplina, verbose_name='Disciplina')
	assunto = models.CharField(max_length = 200)
	data = models.DateTimeField(default=timezone.now)
	pergunta = RichTextField()
	#alternativas da questo objetiva
	alternativa_a = models.CharField(max_length = 200, blank=True)
	alternativa_b = models.CharField(max_length = 200, blank=True)
	alternativa_c = models.CharField(max_length = 200, blank=True)
	alternativa_d = models.CharField(max_length = 200, blank=True)
	alternativa_e = models.CharField(max_length = 200, blank=True)
	alternativa_correta = models.CharField(max_length = 200, blank=True)
	def __str__(self):
		return self.assunto.encode('utf8')


class Pergunta_Certo_Errado(models.Model):
	"""docstring for Pergunta"""
	author = models.ForeignKey('auth.User')
	disciplina = models.ForeignKey(Disciplina, verbose_name='Disciplina')
	assunto = models.CharField(max_length = 200)
	data = models.DateTimeField(default=timezone.now)
	pergunta = models.TextField()
	certo_errado= models.CharField(max_length = 200, blank=True)
	def __str__(self):
		return self.assunto.encode('utf8')

class Pergunta_Subjetiva(models.Model):
	"""docstring for Pergunta"""
	author = models.ForeignKey('auth.User')
	disciplina = models.ForeignKey(Disciplina, verbose_name='Disciplina')
	assunto = models.CharField(max_length = 200)
	data = models.DateTimeField(default=timezone.now)
	pergunta = models.TextField()
	def __str__(self):
		return self.assunto.encode('utf8')

class Prova_Selecionada(models.Model):
	"""docstring for Prova_Selecionada"""
	questoes = models.CharField(max_length = 200)
	nome_prova = models.CharField(max_length = 200, blank=True)
	data = models.DateTimeField(default=timezone.now)
	#turma a qual a prova sera aplicada
	grupo = models.ForeignKey('auth.Group')
	def __str__(self):
		return self.nome_prova.encode('utf8')

class Resposta(models.Model):
	"""docstring for Respostas"""
	prova_selecionada = models.ForeignKey(Prova_Selecionada, verbose_name='Prova_Selecionada')
	respostas = models.CharField(max_length = 200)
	author = models.ForeignKey('auth.User')
	data = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.nome_aluno.encode('utf8')



		