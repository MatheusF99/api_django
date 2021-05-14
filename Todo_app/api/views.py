from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.views import APIView
import json

from .models import Author, Tasks
from .serializers import AuthorCreateSerializers, AuthorListSerializer, CreateTaskSerializer

from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your views here.


# view de teste
class welcome(APIView):

    def get(self, request, format=None):
        user = request.user.id
        content = {"hello": user}
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

            user = User.objects.create_user(
                username=payload['author_nick'],
                email=payload['author_email'],
                password=payload['author_password']
            )
            user.save()

            # payloader = jwt_payload_handler(author)
            # token = jwt_encode_handler(payloader)

            # print(token)

            return JsonResponse({'Author': serializers.data}, safe=False, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse({'error': 'erro ao criar o usuario'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# lista usuarios
class ListAuthorView(APIView):
    def get(selfr, request, format=None):
        author = Author.objects.all()
        serializers = AuthorListSerializer(author, many=True)

        return JsonResponse({'Author': serializers.data}, safe=False, status=status.HTTP_200_OK)

# atualiza usuario


# deleta usuario
class DeleteAuthorView(APIView):
    def delete(self, request, author_id, format=None):
        author = Author.objects.filter(author_id=author_id)

        try:
            author.delete()
            return JsonResponse({'Deleted': 'author deletado com sucesso'}, safe=False, status=status.HTTP_200_OK)
        except:
            return JsonResponse({'ERROR': 'internal server error'}, safe=False, status=status.status.HTTP_500_INTERNAL_SERVER_ERROR)

# Tasks


class CreateTaskView(APIView):
    def post(self, request, format=None):
        payload = json.loads(request.body)
        user = request.user.id
        print(user, payload)

        # try:
        #     pass
        # except:
        #     pass
        return user
