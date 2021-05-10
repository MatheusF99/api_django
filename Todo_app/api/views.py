from django.http import JsonResponse
from rest_framework.views import APIView
import json

from .models import Author, Tasks
from .serializers import AuthorCreateSerializers

from rest_framework import status

# Create your views here.


class welcome(APIView):
    def get(self, request, format=None):
        content = {"hello": "world"}
        return JsonResponse(content)


# criar usuario
class CreateAuthorView(APIView):
    def post(self, request, format=None):
        payload = json.loads(request.body)
        print(request)

        try:
            author = Author(
                author_nick=payload['author_nick'],
                author_email=payload['author_email'],
                author_password=payload['author_password']
            )

            author.save()
            serializers = AuthorCreateSerializers(author)

            return JsonResponse({'Author': serializers.data}, safe=False, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse({'error': 'erro ao criar o usuario'}, safe=False, status=status.status.HTTP_500_INTERNAL_SERVER_ERROR)


# lista usuarios
class ListAuthorView(APIView):
    def get(request):
        pass
