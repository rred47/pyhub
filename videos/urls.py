"""Video URLS Config"""
from django.urls import path
from .views import CategoryList, VideoList, VideoDetail

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('videos/', VideoList.as_view(), name='video_list'),
    path('videos/<int:video_pk>', VideoDetail.as_view(), name='video_detail'),
]
