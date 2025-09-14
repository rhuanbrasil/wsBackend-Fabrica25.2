from rest_framework import viewsets
from ..models import Resenha
from ..serializers.resenhaSerializer import ResenhaSerializer

class ResenhaViewSet(viewsets.ModelViewSet):
    queryset = Resenha.objects.all()
    serializer_class = ResenhaSerializer