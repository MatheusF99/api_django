from django.urls import path
from .views import welcome, CreateAuthorView

urlpatterns = [
    path('welcome', welcome.as_view()),
    path('create_author', CreateAuthorView.as_view())
]
