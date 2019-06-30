from django.urls import path

from.import views

urlpatterns = [
	path('',views.index, name='index'),
    path('<int:Categoria_id>/categorias/', views.detail, name='detail'),
    path('<int:Pergunta_id>/perguntas/', views.question, name='question'),
    path('<int:Resposta_id>/respostas/', views.answer, name='answer'),
	path('<str:Categoria_nome>/<int:dificuldade>/', views.test, name='test'),
	path('voce_perdeu/', views.fim_de_jogo, name='fim_de_jogo'),
	path('vitoria/',views.voce_ganhou, name='voce_ganhou'),
]