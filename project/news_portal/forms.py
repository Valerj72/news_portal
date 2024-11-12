from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'article_title',
            'category',
        ]

    class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = [
                'article_title',
                'category',
            ]

    def clean_data(self):
        article_title = self.cleaned_data["article_title"]
        if article_title[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return article_title