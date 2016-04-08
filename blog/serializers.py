from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Categories

class CategorySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Categories
		fields = ('id', 'category',)

class PostSerializer(serializers.ModelSerializer):
	# Can't be True because User is not iterable
	author = serializers.StringRelatedField(many=False)
	class Meta:
		model = Post
		fields = ('id', 'author','title', 'subtitle', 'slug', 'image', 'height_field', 'width_field',)
