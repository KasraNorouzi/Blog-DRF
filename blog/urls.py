from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
app_name = 'blog'

urlpatterns = [
    # path('go-to-maktabkhooneh/<int:pk>/', views.RedirectToMaktab.as_view()),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]