from django.conf.urls import url
from django.urls import path
from .views import welcome, CreateAuthorView, ListAuthorView, DeleteAuthorView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('welcome', welcome.as_view()),
    url(r'^login/', obtain_jwt_token),
    # author
    path('create_author', CreateAuthorView.as_view()),
    path('list_author', ListAuthorView.as_view()),
    path('delete_author/<uuid:author_id>', DeleteAuthorView.as_view())
    # task
]
