""" View for videos. """
from django.shortcuts import render, redirect
from django.http import Http404
from django.views import View
from .models import Category, Video
from .forms import CategoryForm, VideoForm


class CategoryList(View):
    model_class = Category
    """Category list view."""

    def get(self, request):
        """
        Get category list.

        :param: request :Request
        """
        categories = self.model_class.objects.all()
        form = CategoryForm()
        context = {
            'categories': categories,
            'form': form,
        }
        return render(request, template_name='videos/categories.html', context=context)

    def post(self, request):
        """
        Create category.

        :param: request :Request
        """
        form = CategoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='category_list')
        categories = self.model_class.objects.all()
        context = {
            'categories': categories,
            'form': form,
        }
        return render(request=request, template_name='videos/categories.html', context=context)


class VideoList(View):
    model_class = Video
    """Video list view."""

    def get(self, request):
        """
        Get video list.

        :param: request :Request
        """
        videos = self.model_class.objects.all()
        form = VideoForm()
        context = {
            'videos': videos,
            'form': form,
        }
        return render(request, template_name='videos/videos.html', context=context)

    def post(self, request):
        """
        Create video.

        :param: request :Request
        """
        form = VideoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='video_list')
        videos = self.model_class.objects.all()
        context = {
            'videos': videos,
            'form': form,
        }
        return render(request=request, template_name='videos/videos.html', context=context)

class VideoDetail(View):
    """Video detail view."""

    model_class = Video

    def get(self, request, video_pk: int):
        try:
            video = self.model_class.objects.get(pk=video_pk)
        except Video.DoesNotExist:
            raise Http404()
            
        context = {
            'video': video,
        }
        return render(request=request, template_name='videos/video.html', context=context)