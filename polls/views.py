from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def detail (request, Categoria_id):
    return HttpResponse("Você está vendo a categoria %s." % Categoria_id)

def question (request, Pergunta_id):
    return HttpResponse("Você está vendo a pergunta %s." % Pergunta_id)

def answer (request, Resposta_id):
    resposta = "Você está vendo a resposta %s."
    return HttpResponse(resposta%Resposta_id)