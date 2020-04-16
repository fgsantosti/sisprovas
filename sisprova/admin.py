# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Disciplina, Pergunta_Objetiva, Pergunta_Certo_Errado, Pergunta_Subjetiva,Prova_Selecionada, Resposta

# Register your models here.
admin.site.register(Disciplina)
admin.site.register(Pergunta_Objetiva)
admin.site.register(Pergunta_Certo_Errado)
admin.site.register(Pergunta_Subjetiva)
admin.site.register(Prova_Selecionada)
admin.site.register(Resposta)
