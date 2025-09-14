from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from rest_framework.routers import DefaultRouter
from .modelViewSets import modelViewSet_livro, modelViewSet_resenha
from .views import BuscaGoogleBooksView, LivroDetailView

router = DefaultRouter()
router.register(r'livros', modelViewSet_livro.LivroViewSet, basename='livro')
router.register(r'resenhas', modelViewSet_resenha.ResenhaViewSet, basename='resenha')

urlpatterns = [
    path('', RedirectView.as_view(url='/estante/', permanent=True), name='home'),
    path('busca/', TemplateView.as_view(template_name='core/busca.html'), name='busca'),
    path('estante/', TemplateView.as_view(template_name='core/estante.html'), name='estante'),
    
    path('api/', include(router.urls)), 
    
    path('livros/<int:pk>/', LivroDetailView.as_view(), name='livro-detail'),

    path('api/buscar-livros/', BuscaGoogleBooksView.as_view(), name='buscar-livros-api'),
]

