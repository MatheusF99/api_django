from django.db.models import fields
from rest_framework import serializers
from .models import Author, Tasks


class AuthorCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_nick', 'author_email', 'author_password')


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id', 'author_nick', 'author_email')
