from django.rest_framework import serializers
from estante_virtual.core.models import Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'título', 'autor', 'google_books_id', 'url_capa', 'ano_publicacao']

