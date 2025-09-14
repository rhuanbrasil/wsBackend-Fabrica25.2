from django.rest_framework import ModelViewSet
from estante_virtual.core.models import Resenha
from estante_virtual.core.serializers.resenhaSerializer import ResenhaSerializer

class ResenhaViewSet(ModelViewSet):
    queryset = Resenha.objects.all()
    serializer_class = ResenhaSerializer