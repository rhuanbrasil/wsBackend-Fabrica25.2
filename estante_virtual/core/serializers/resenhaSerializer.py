from django.rest_framework import serializers
from estante_virtual.core.models import Resenha

class ResenhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resenha
        fields = ['id', 'livro', 'comentario', 'nota', 'data_criacao']