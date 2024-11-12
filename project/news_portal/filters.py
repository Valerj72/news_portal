from django_filters import FilterSet, DateFilter
from django import forms
from .models import Post

date = DateFilter(
    field_name='time_in',
    lookup_expr='gt',
    label='Date',
    widget=forms.DateInput(attrs={'type': 'date'})
)

class PostFilter(FilterSet):
    class Meta:
       model = Post
       fields = {
           'article_title',
           'category',
           'time_in'
       }