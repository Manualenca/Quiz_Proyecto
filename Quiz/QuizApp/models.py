from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CategoryPreguntaManager (models.Manager):
    '''Manager para obtener todas las posibles categorias 
    de preguntas del juego'''
    name=models.Charfield(max_length=250)

    def get_queryset(self):
        return super().get_queryset().filter(category)


class SubcategoryPreguntasManager(models.Manager):
    '''Manager para obtener todas las preguntas relacionadas
    con ciencias'''
    name= models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def get_queryset(self):
        return super().get_queryset().filter(category=subcategory)

#class CursoByTopicManager(models.Manager):
    """Manager para obtener todas las preguntas que no son 
    de ciencias."""

    #def get_queryset(self):
        #return super().get_queryset().filter(categorias=entretenimiento)

class QuestionPreguntasManager(models.Manager):
    question = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)
    correct_answer = models.CharField(max_length=255)
    incorrect_answers = models.TextField()
    type = models.CharField(max_length=20, choices=[('multiple', 'Multiple'), ('boolean', 'Boolean')])
    difficulty = models.CharField(max_length=10, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])      

class Partida(models.Model):
    jugador = models.CharField(max_length=255)  
    preguntas = models.ManyToManyField(Question, related_name='partidas')
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    puntaje = models.IntegerField(default=0)

class PreguntaPartida(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Question, on_delete=models.CASCADE)
    respuesta_seleccionada = models.CharField(max_length=255, blank=True, null=True)



#class CustomUser(AbstractUser):
    #JUGADOR = 'is_jugador'
    #EDITOR = 'is_editor'

    #ROLE_CHOICES =[
       #(JUGADOR, 'is_jugador'),
        #(EDITOR, 'is_editor'),
    #]
    #role = models.CharField(max_length=10, choices=ROLE_CHOICES, default= is_jugador) 

    #a continuación lo consulte con Youtube y Chat gpt
    
class User(AbstractUser):
    is_jugador = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)

class Jugador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    juegos_jugados = models.IntegerField(default=0)
    puntuacion_total = models.IntegerField(default=0)
    juegos_ganados = models.IntegerField(default=0)
    juegos_perdidos = models.IntegerField(default=0)
    racha_ganadora_mas_larga = models.IntegerField(default=0)
    fecha_ultimo_juego = models.DateField(blank=True, null=True)

   
    def __str__(self):
        return f"{self.nombre}"

class Editor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preguntas_creadas = models.IntegerField(default=0)
    preguntas_editadas = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.nombre} ({self.email})"

#class Juego(models.Model):
    #jugador= models.ForeignKey(Jugador, on_delete=models.CASCADE)
    #juego= models.ForeignKey(Juego, on_delete=models.CASCADE)
    
    #fecha_inscripcion = models.DateField(auto_now_add=True)

    #def __str__(self):
       # return f"{self.jugador} inscrito en {self.curso}"