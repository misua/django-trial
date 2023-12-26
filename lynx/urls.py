from django.urls import path
from.views import ArticleDeleteView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete-view'),
    # path('cancel_delete/', views.cancel_delete, name='cancel-delete'),
    path('article/<int:pk>/',views.singular_article, name='article'),
]