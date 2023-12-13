# Generated by Django 5.0 on 2023-12-12 23:16

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_jugador', models.BooleanField(default=False)),
                ('is_editor', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
                ('puntaje', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preguntas_creadas', models.IntegerField(default=0)),
                ('preguntas_editadas', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juegos_jugados', models.IntegerField(default=0)),
                ('puntuacion_total', models.IntegerField(default=0)),
                ('juegos_ganados', models.IntegerField(default=0)),
                ('juegos_perdidos', models.IntegerField(default=0)),
                ('racha_ganadora_mas_larga', models.IntegerField(default=0)),
                ('fecha_ultimo_juego', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPreguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('correct_answer', models.CharField(max_length=255)),
                ('incorrect_answers', models.TextField()),
                ('type', models.CharField(choices=[('multiple', 'Multiple'), ('boolean', 'Boolean')], max_length=20)),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuizApp.categorypregunta')),
            ],
        ),
        migrations.CreateModel(
            name='PreguntaPartida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_seleccionada', models.CharField(blank=True, max_length=255, null=True)),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuizApp.partida')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuizApp.questionpreguntas')),
            ],
        ),
        migrations.AddField(
            model_name='partida',
            name='preguntas',
            field=models.ManyToManyField(related_name='partidas', to='QuizApp.questionpreguntas'),
        ),
        migrations.CreateModel(
            name='SubcategoryPreguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuizApp.categorypregunta')),
            ],
        ),
        migrations.AddField(
            model_name='questionpreguntas',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='QuizApp.subcategorypreguntas'),
        ),
    ]
