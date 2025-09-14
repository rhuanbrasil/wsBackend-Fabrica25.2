from rest_framework import viewsets
from ..models import Livro
from ..serializers.livroSerializer import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

