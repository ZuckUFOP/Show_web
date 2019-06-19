from django.urls import path

from.import views

urlpatterns = [
    path('<int:Categoria_id>/', views.detail, name='detail'),
    path('<int:Pergunta_id>/question/', views.question, name='question'),
    path('<int:Resposta_id>/answer/', views.answer, name='answer'),
]