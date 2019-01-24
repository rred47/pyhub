from django import forms
from .models import Category, Video


class CategoryForm(forms.ModelForm):
    """Form for category model."""

    name = forms.CharField(required=True, max_length=12)
    cover = forms.ImageField(required=True)

    class Meta:
        model = Category
        fields = ['name', 'cover']


class VideoForm(forms.ModelForm):
    """Form for video model."""

    category = forms.ModelChoiceField(queryset=Category.objects.all())
    name = forms.CharField()
    cover = forms.ImageField()
    file = forms.FileField()
    views = forms.IntegerField()
    is_private = forms.BooleanField(required=False)

    class Meta:
        model = Video
        fields = ['category', 'name', 'cover', 'file', 'views', 'is_private']
