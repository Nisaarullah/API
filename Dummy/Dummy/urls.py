from django.urls import path
from yummy.views import UserListCreateView, UserRetrieveView, CategoryListCreateView, CategoryRetrieveView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveView.as_view(), name='user-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveView.as_view(), name='category-detail'),
]
