from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Author
       fields = ['id', 'name', ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Category
       fields = ['id', 'grade', ]


class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Subscriber
       fields = ['id', 'name', ]


class PostSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Post
       fields = ['id', 'name', ]


class PostCategorySerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = PostCategory
       fields = ['id', 'name', ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Comment
       fields = ['id', 'name', ]
