from django.db import models
# generate uuid code
import uuid
# generate date time
from django.utils import timezone


# Create your models here.
# criando model de usuario
class Author(models.Model):
    author_id = models.UUIDField(
        unique=True,
        null=False,
        default=uuid.uuid4,
        editable=False,
        primary_key=True
    ),
    author_nick = models.CharField(max_length=100, null=False, unique=False),
    author_email = models.EmailField(unique=True, null=False),
    author_password = models.CharField(max_length=255, null=False)
    create_at = models.DateField(default=timezone.now)

    def __str__(self):
        return "<author %s>" % self.author_nick


# criando o model de task
class Tasks(models.Model):
    id = models.UUIDField(
        null=False,
        unique=True,
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    task_title = models.CharField(max_length=255, null=False)
    task_content = models.CharField(max_length=255, null=False)
    task_data = models.CharField(max_length=10, null=False)
    task_hour = models.CharField(null=False, max_length=5)
    task_remember = models.BooleanField(default=False)
    task_completed = models.BooleanField(default=False)
    task_created = models.DateTimeField(default=timezone.now, blank=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __repr__(self):
        return "<Task %s>" % self.id
