from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.views.generic import DetailView
from .models import Livro


class BuscaGoogleBooksView(APIView):
    def get(self, request):
    
        titulo = request.query_params.get('titulo', None)

        if not titulo:
            return Response(
                {"erro": "O parâmetro 'titulo' é obrigatório."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        url_base = 'https://www.googleapis.com/books/v1/volumes'
        
        params = {
            'q': f'intitle:{titulo}',
        }
        
        try:
            response = requests.get(url_base, params=params)
            response.raise_for_status() 
            
            data = response.json()
            print("--- RESPOSTA DA API DO GOOGLE ---")
            print(data)

            livros_tratados = []
            
            for item in data.get('items', []):
                volume_info = item.get('volumeInfo', {})
                
                titulo_livro = volume_info.get('title', 'Título não disponível')
                
                autores = volume_info.get('authors', ['Autor desconhecido'])
                autores_str = ", ".join(autores)
                
                google_books_id = item.get('id', 'ID não disponível')
                
                image_links = volume_info.get('imageLinks', {})
                url_capa = image_links.get('thumbnail', None)

                livros_tratados.append({
                    'titulo': titulo_livro,
                    'autores': autores_str,
                    'google_books_id': google_books_id,
                    'url_capa': url_capa
                })
                
            return Response(livros_tratados, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response(
                {"erro": f"Ocorreu um erro na comunicação com a Google Books API: {e}"},
                status=status.HTTP_502_BAD_GATEWAY 
            )
class LivroDetailView(DetailView):
    model = Livro
    template_name = 'core/livro_detail.html' 
    context_object_name = 'livro'