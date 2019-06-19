from django.db import models

# Create your models here.
class Categoria(models.Model):
	nome_categoria = models.CharField(max_length=20)
	def __str__(self):
		return self.nome_categoria

class Pergunta(models.Model):
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	texto_da_pergunta = models.CharField(max_length=200)
	dificuldade = models.IntegerField(default=1)
	def __str__(self):
		return self.texto_da_pergunta

class Resposta(models.Model):
	pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
	texto_da_resposta = models.CharField(max_length=200)
	validade = models.BooleanField(default=False)
	def __str__(self):
		return self.texto_da_resposta
	def e_verdade(self):
		return self.validade