from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'article_title',
            'article_text',
            'category',
        ]

    def clean_article_title(self):
        article_title = self.cleaned_data["article_title"]
        if article_title[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return article_title