from rest_framework import serializers
from ..models import Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'título', 'autor', 'google_books_id', 'url_capa', 'ano_publicacao']

