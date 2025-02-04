
from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post, Comment, LikeComment
from rest_framework.request import Request




from django.contrib.auth.models import User
class PostSerializer(serializers.ModelSerializer):
    #comments = CommentSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'

    def get_comments(self, obj):
        from .serializers import CommentSerializer  # Import inside method
        return CommentSerializer(obj.comments.all(), many=True, context=self.context).data


class LikeCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LikeComment
        fields = ['user', 'comment', 'created_at']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'posts']

    def get_posts(self, obj):
        from .serializers import PostSerializer  # Import inside method
        return PostSerializer(obj.posts.all(), many=True, context=self.context).data

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    comment_likes = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_comment_likes(self, obj):
        from .serializers import LikeCommentSerializer
        # Return the list of likes or just the count
        return LikeCommentSerializer(obj.comment_likes.all(), many=True, context=self.context).data

