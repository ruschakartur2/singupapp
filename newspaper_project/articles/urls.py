from django.urls import path

from .views import (ArticleListView,
                    ArticleListCreate,
                    ArticleUpdateView,
                    ArticleDetailView,
                    ArticleDeleteView)

urlpatterns = [
    path('new/', ArticleListCreate.as_view(), name = 'article_create'),
    path('<int:pk>/edit/',ArticleUpdateView.as_view(),name = 'article_edit'),
    path('<int:pk>/',ArticleDetailView.as_view(),name = 'article_detail'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name = 'article_delete'),
    path('',ArticleListView.as_view(), name='article_list')
]