from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from random import randint

from .models import Categoria, Pergunta, Resposta

# Create your views here.
def index (request):
	lista_categoria = Categoria.objects.order_by('-id')[:4]
	template=loader.get_template('polls/index.html')
	contex = { 'lista_categoria': lista_categoria}
	return HttpResponse(template.render(contex, request))

def detail (request, Categoria_id):
    return HttpResponse("Você está vendo a categoria %s." % Categoria_id)

def question (request, Pergunta_id):
    return HttpResponse("Você está vendo a pergunta %s." % Pergunta_id)

def answer (request, Resposta_id):
    resposta = "Você está vendo a resposta %s."
    return HttpResponse(resposta%Resposta_id)

def test (request, Categoria_nome, dificuldade):
	template=loader.get_template('polls/perguntas.html')
	lista_de_perguntas = Pergunta.objects.order_by("dificuldade")
	perguntas = []
	lista_de_respostas = Resposta.objects.order_by("-id")
	respostas = []
	for k in lista_de_perguntas:
		if (k.dificuldade == dificuldade)and(Categoria_nome == k.categoria.nome_categoria):
			perguntas.append(k)
	num = randint(0,len(perguntas)-1)
	for k in lista_de_respostas:
		if k.pergunta == perguntas[num]:
			respostas.append(k)
	contex = {'pergunta':perguntas[num], 'lista_de_respostas':respostas}
	return HttpResponse(template.render(contex, request))

def fim_de_jogo(request):
	template=loader.get_template('polls/derrota.html')
	contex = {}
	return HttpResponse(template.render(contex,request))

def voce_ganhou(request):
	template=loader.get_template('polls/vitoria.html')
	contex = {}
	return HttpResponse(template.render(contex,request))