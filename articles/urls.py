from django.urls import path

from .views import(
    article_list,
    article_detail,
    article_create,
)

app_name = 'articles'

urlpatterns = [
    path('', article_list, name='article-list'),
    path('create/', article_create, name='article-create'),
    path('<slug:slug>', article_detail, name='article-detail'),
]
