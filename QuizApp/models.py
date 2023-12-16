from typing import Any
#from django.contrib.auth.models import User
from django.db import models
from Account.models import UserModel

class CategoryPregunta(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class SubcategoryPreguntas(models.Model):
    category = models.ForeignKey(CategoryPregunta, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.category

class QuestionPreguntas(models.Model):
    question = models.TextField()
    category = models.ForeignKey(CategoryPregunta, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubcategoryPreguntas, on_delete=models.CASCADE, blank=True, null=True)
    correct_answer = models.CharField(max_length=255)
    incorrect_answers = models.TextField()
    type = models.CharField(max_length=20, choices=[('multiple', 'Multiple'), ('boolean', 'Boolean')])
    difficulty = models.CharField(max_length=10, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])


    def __str__(self):
        return self.question
class Partida(models.Model):
    jugador = models.ForeignKey(UserModel, on_delete= models.CASCADE)
    preguntas = models.ManyToManyField(QuestionPreguntas, related_name='partidas')
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    puntaje = models.IntegerField(default=0)

    def __str__(self):
        return self.jugador

class PreguntaPartida(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(QuestionPreguntas, on_delete=models.CASCADE)
    respuesta_seleccionada = models.CharField(max_length=255, blank=True, null=True)
    ordering = models.IntegerField()
    
    def __str__(self):
        return self.partida

class Jugador(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    juegos_jugados = models.IntegerField(default=0)
    puntuacion_total = models.IntegerField(default=0)
    juegos_ganados = models.IntegerField(default=0)
    juegos_perdidos = models.IntegerField(default=0)
    racha_ganadora_mas_larga = models.IntegerField(default=0)
    fecha_ultimo_juego = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"

class Editor(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    preguntas_creadas = models.IntegerField(default=0)
    preguntas_editadas = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}"
