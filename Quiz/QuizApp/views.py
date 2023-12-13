from django.http import HttpResponse
import datetime
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from .models import Question, Partida

def welcome(request):
    now = datetime.datetime.now()
    return HttpResponse(f"Hola, es hora de jugar al Preguntado. La hora del servidor es  {now.strftime('%A, %d %B, %Y a las %X')}.")


class ListaPreguntasView(ListView):
    model = Question
    template_name = 'preguntas/lista_preguntas.html'
    context_object_name = 'preguntas'

class DetallePreguntaView(DetailView):
    model = Question
    template_name = 'preguntas/detalle_pregunta.html'
    context_object_name = 'pregunta'

class ListaPartidasView(ListView):
    model = Partida
    template_name = 'preguntas/lista_partidas.html'
    context_object_name = 'partidas'
