from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Author
       fields = "__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Category
       fields = "__all__"


class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Subscriber
       fields = "__all__"


class PostSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Post
       fields = "__all__"


class PostCategorySerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = PostCategory
       fields = "__all__"


class CommentSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Comment
       fields = "__all__"
