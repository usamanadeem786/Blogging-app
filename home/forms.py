from django import forms
from .models import Post

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image']