from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post



from django.contrib.auth.models import User
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'posts']

