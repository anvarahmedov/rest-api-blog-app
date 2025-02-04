from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']


from django.contrib.auth.models import User
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
