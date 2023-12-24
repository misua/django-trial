from django.urls import path
from.views import ArticleDeleteView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article-delete'),
    
]