from django.urls import path
from .views import welcome, CreateAuthorView, ListAuthorView, DeleteAuthorView

urlpatterns = [
    path('welcome', welcome.as_view()),
    # author
    path('create_author', CreateAuthorView.as_view()),
    path('list_author', ListAuthorView.as_view()),
    path('delete_author/<uuid:author_id>', DeleteAuthorView.as_view())
    # task
]
