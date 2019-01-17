"""Video URLS Config"""
from django.urls import path
from .views import CategoryList

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category_list'),
]

