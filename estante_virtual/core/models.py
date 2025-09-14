from django.db import models

class Livro(models.Model):
    título = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    google_books_id = models.CharField(max_length=50, unique=True)
    url_capa = models.URLField(max_length=200)
    ano_publicacao = models.IntegerField()
    

    def __str__(self):
        return self.título, self.autor, self.google_books_id, self.url_capa, self.ano_publicacao
    
class Resenha(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='resenhas')
    comentario = models.TextField()
    nota = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comentario, self.nota, self.livro, self.data_criacao