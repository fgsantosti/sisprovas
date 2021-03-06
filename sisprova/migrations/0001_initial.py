# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-04 17:46
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta_Certo_Errado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=200)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('pergunta', models.TextField()),
                ('certo_errado', models.CharField(blank=True, max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sisprova.Disciplina', verbose_name='Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta_Objetiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=200)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('pergunta', ckeditor.fields.RichTextField()),
                ('alternativa_a', models.CharField(blank=True, max_length=200)),
                ('alternativa_b', models.CharField(blank=True, max_length=200)),
                ('alternativa_c', models.CharField(blank=True, max_length=200)),
                ('alternativa_d', models.CharField(blank=True, max_length=200)),
                ('alternativa_e', models.CharField(blank=True, max_length=200)),
                ('alternativa_correta', models.CharField(blank=True, max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sisprova.Disciplina', verbose_name='Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta_Subjetiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=200)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('pergunta', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sisprova.Disciplina', verbose_name='Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Prova_Selecionada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questoes', models.CharField(max_length=200)),
                ('nome_prova', models.CharField(blank=True, max_length=200)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respostas', models.CharField(max_length=200)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('nome_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('prova_selecionada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sisprova.Prova_Selecionada', verbose_name='Prova_Selecionada')),
            ],
        ),
    ]
