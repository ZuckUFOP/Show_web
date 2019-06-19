from django.contrib import admin
from .models import Categoria, Pergunta, Resposta

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Pergunta)
admin.site.register(Resposta)