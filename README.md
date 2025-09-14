# 📖 Estante Virtual

![Django](https://img.shields.io/badge/Django-5.2-blue?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![DRF](https://img.shields.io/badge/Django%20REST-3.16-red?style=for-the-badge)

Projeto de uma aplicação web completa para busca, catalogação e avaliação de livros, desenvolvido como parte de um projeto de extensão universitária. A aplicação utiliza o Django e Django REST Framework no backend para criar uma API RESTful e templates dinâmicos no frontend que consomem essa mesma API, além de integrar-se com a API externa do Google Books.

---


## 📌 Sobre o Projeto

A **Estante Virtual** é uma solução para amantes da leitura que desejam organizar e avaliar seus livros. O usuário pode buscar por qualquer livro utilizando a vasta base de dados do Google Books, adicioná-lo à sua estante pessoal, visualizar sua coleção e escrever resenhas com notas para cada obra lida.

O projeto foi construído seguindo as melhores práticas do Django, com uma clara separação entre a lógica da API (servida pelo Django REST Framework) e a apresentação (servida pelos templates do Django com JavaScript vanilla), demonstrando um ciclo de desenvolvimento full-stack.

---

## ✨ Funcionalidades

-   [x] **Busca de Livros:** Pesquisa em tempo real na API do Google Books por título.
-   [x] **Estante Pessoal:** Adiciona livros encontrados à uma estante virtual, salvando-os no banco de dados local.
-   [x] **Visualização da Coleção:** Galeria com todos os livros salvos pelo usuário.
-   [x] **Detalhes do Livro:** Página dedicada com informações detalhadas de cada livro.
-   [x] **Sistema de Resenhas:** Adição de comentários e notas (1 a 5) para cada livro na estante.
-   [x] **API RESTful:** Endpoints para gerenciar livros e resenhas (CRUD).

---

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

* **Backend:**
    * [Python 3](https://www.python.org/)
    * [Django](https://www.djangoproject.com/)
    * [Django REST Framework](https://www.django-rest-framework.org/)
    * [Requests](https://requests.readthedocs.io/en/latest/)

* **Frontend:**
    * HTML5
    * CSS3
    * JavaScript (Vanilla) com Fetch API

* **Banco de Dados:**
    * SQLite 3 (padrão do Django)

* **APIs Externas:**
    * [Google Books API](https://developers.google.com/books)

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* [Python 3](https://www.python.org/)
* [Git](https://git-scm.com/) (opcional, mas recomendado)

### Rodando o Projeto

```bash
# 1. Clone o repositório
$ git clone [https://github.com/rhuanbrasil/wsBackend-Fabrica25.2)

# 2. Navegue até o diretório do projeto
$ cd estante-virtual

# 3. Crie e ative um ambiente virtual
# No Windows
$python -m venv venv$ venv\Scripts\activate
# No macOS/Linux
$python3 -m venv venv$ source venv/bin/activate

# 4. Crie o arquivo requirements.txt (se ainda não existir)
$ pip freeze > requirements.txt
# (Ele deve conter django, djangorestframework, requests, etc.)

# 5. Instale as dependências
$ pip install -r requirements.txt

# 6. Aplique as migrações do banco de dados
$ python manage.py migrate

# 7. Inicie o servidor de desenvolvimento
$ python manage.py runserver

# 8. Abra seu navegador e acesse a aplicação
Acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
```

---

## 🔗 Endpoints da API

A API RESTful oferece os seguintes endpoints para manipulação dos dados:

| Endpoint                  | Método HTTP | Descrição                                        |
| ------------------------- | ----------- | -------------------------------------------------- |
| `/api/livros/`              | `GET`       | Lista todos os livros da estante.                  |
| `/api/livros/`              | `POST`      | Adiciona um novo livro à estante.                  |
| `/api/livros/<id>/`         | `GET`       | Retorna os detalhes de um livro específico.        |
| `/api/resenhas/`            | `GET`       | Lista todas as resenhas. |
| `/api/resenhas/`            | `POST`      | Cria uma nova resenha para um livro.               |
| `/api/buscar-livros/`     | `GET`       | Busca livros na API do Google. Ex: `?titulo=Python`|

---

## 📸 Telas da Aplicação

<p align="center">
  <img src="https://imgur.com/ZrRYpLi.png" width="400" title="Tela de Busca">
  <img src="https://imgur.com/vPYNWBm.png" width="400" title="Tela da Estante">
</p>
<p align="center">
  <em>Tela de Busca e Tela da Estante Pessoal</em>
</p>

---

<p align="center">
  Feito por <strong>Rhuan Brasil</strong>
</p>
