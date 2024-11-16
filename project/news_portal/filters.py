from django_filters import FilterSet, DateFilter
from django import forms
from .models import Post


class PostFilter(FilterSet):
    class Meta:
       model = Post
       fields = {
           'article_title',
           'category',
       }

    date = DateFilter(
       field_name='time_in',
       lookup_expr='gt',
       label='Date',
       widget=forms.DateInput(attrs={'type': 'date'})
    )