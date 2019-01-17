from django.shortcuts import render, redirect
from django.views import View
from .models import Category
from .forms import CategoryForm

class CategoryList(View):
    """Category list view."""

    def get(self, request):
        """
        Get category list.

        :param: request :Request
        """
        categories = Category.objects.all()
        form = CategoryForm()
        context = {
            'categories': categories,
            'form': form,
        }
        return render(request, template_name='videos/list.html', context=context)
    
    def post(self, request):
        """
        Create category.

        :param: request :Request
        """
        form = CategoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='category_list')
        categories = Category.objects.all()
        context = {
            'categories': categories,
            'form': form,
        }
        return render(request=request, template_name='videos/list.html', context=context)