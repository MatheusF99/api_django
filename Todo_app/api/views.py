from django.http import JsonResponse
from rest_framework.views import APIView

# Create your views here.


class welcome(APIView):
    def get(self, request, format=None):
        content = {"hello": "world"}
        return JsonResponse(content)
