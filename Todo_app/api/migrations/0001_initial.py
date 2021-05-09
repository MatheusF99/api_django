# Generated by Django 3.2 on 2021-05-09 21:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_password', models.CharField(max_length=255)),
                ('create_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('task_title', models.CharField(max_length=255)),
                ('task_content', models.CharField(max_length=255)),
                ('task_data', models.CharField(max_length=10)),
                ('task_hour', models.CharField(max_length=5)),
                ('task_remember', models.BooleanField(default=False)),
                ('task_completed', models.BooleanField(default=False)),
                ('task_created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.author')),
            ],
        ),
    ]
