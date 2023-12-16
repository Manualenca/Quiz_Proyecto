from django.contrib import admin
from .models import (
    CategoryPregunta,
    SubcategoryPreguntas,
    QuestionPreguntas,
    Partida,
    PreguntaPartida,
    Jugador,
    Editor,
)

# Register your models here.

admin.site.register(CategoryPregunta)
admin.site.register(SubcategoryPreguntas)
admin.site.register(QuestionPreguntas)
admin.site.register(Partida)
admin.site.register(PreguntaPartida)
admin.site.register(Jugador)
admin.site.register(Editor)
