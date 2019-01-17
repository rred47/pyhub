from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
  """Form for category."""

  name = forms.CharField(required=True, max_length=12)
  cover = forms.ImageField(required=True)

  class Meta:
    model = Category
    fields = ['name', 'cover']
