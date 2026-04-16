# Create your models here. / forma como o sistema conversa com o banco de dados.

from django.db import models

class Curso(models.Model): # Classe = Modelo
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()
    nivel = models.CharField(max_length=50)

    carga_horaria = models.IntegerField()

    def __str__(self): # Equivalente ao GETTER (POO)
        return self.nome # Indicador do objeto

class Avaliacao(models.Model):
    # Uma tupla de opções para o Dropdown / Lista que armazema outras listas
    NOTAS_CHOICES = [
        ('1', '⭐ (1) Ruim'),
        ('2', '⭐⭐ (2) Regular'),
        ('3', '⭐⭐⭐ (3) Bom'),
        ('4', '⭐⭐⭐⭐ (4) Muito Bom'),
        ('5', '⭐⭐⭐⭐⭐ (5) Excelente'),
    ]

    nome_aluno = models.CharField(max_length=100)
    nome_curso = models.ForeignKey(Curso, on_delete=models.CASCADE) # ForeignKey = Engenharia de dados relacionais / Aqui, o atributo nome_curso vira uma lista dos objetos disponiveis do model Curso 
    nota = models.CharField(max_length=1, choices=NOTAS_CHOICES)
    comentario = models.TextField() # TextField = Sem limite / Pode sobrecarregar o banco de dados e dar liberdade para os hackers / Tomar cuidado

    def __str__(self):
        return f"Avaliação de {self.nome_aluno} para o Curso {self.nome_curso} - Nota: {self.nota}"