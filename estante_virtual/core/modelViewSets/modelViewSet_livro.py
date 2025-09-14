from django.rest_framework import ModelViewSet
from estante_virtual.core.models import Livro
from estante_virtual.core.serializers.livroSerializer import LivroSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

