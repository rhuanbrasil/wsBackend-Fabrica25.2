from rest_framework import viewsets
from ..models import Resenha
from ..serializers.resenhaSerializer import ResenhaSerializer

class ResenhaViewSet(viewsets.ModelViewSet):
    serializer_class = ResenhaSerializer

    def get_queryset(self):
    
        queryset = Resenha.objects.all()
        
        livro_id = self.request.query_params.get('livro')
        
        if livro_id is not None:
           
            queryset = queryset.filter(livro__id=livro_id)
            
        return queryset