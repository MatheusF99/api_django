from django.db.models import fields
from rest_framework import serializers
from .models import Author, Tasks


class AuthorCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id', 'author_nick', 'author_email')


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id', 'author_nick', 'author_email')


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('task_title', 'task_content', 'task_data',
                  'task_hour', 'task_remember', 'task_completed', 'author')
