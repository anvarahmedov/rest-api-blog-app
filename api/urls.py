from django.http import HttpResponse, JsonResponse
from django.urls import include, path
import django_filters
from rest_framework import routers

from rest_framework.permissions import IsAuthenticated
from tutorial.quickstart import views

from api.models import User, Post, Comment, LikeComment

from api import serializers
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains', label='Username')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains', label='Email')
    is_active = django_filters.BooleanFilter(field_name='is_active', label='Active Status')
    is_staff = django_filters.BooleanFilter(field_name='is_staff', label='Staff Status')
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff']

class PostModelFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title contains')
    body = django_filters.CharFilter(lookup_expr='icontains', label='Body contains')
    user = django_filters.CharFilter(method='filter_user', label='User ID Filter')
    published_at = django_filters.DateFromToRangeFilter(label='Published Date Range')
    featured = django_filters.BooleanFilter(field_name='featured', label='Is Featured')
    def filter_user(self, queryset, name, value):
        """
        Custom filter for user based on exact, gte, or lte comparison.
        Syntax: user_filter=exact:<id>, user_filter=gte:<id>, or user_filter=lte:<id>
        """
        filter_type, filter_value = value.split(":", 1)
        try:
            user_id = int(filter_value)
        except ValueError:
            return queryset.none()  # Invalid filter value

        if filter_type == 'exact':
            return queryset.filter(user__id=user_id)
        elif filter_type == 'gte':
            return queryset.filter(user__id__gte=user_id)
        elif filter_type == 'lte':
            return queryset.filter(user__id__lte=user_id)
        else:
            return queryset.none()  # Invalid filter type

    class Meta:
        model = Post
        fields = ['title', 'body', 'user', 'published_at', 'featured']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class = UserFilter
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        """Pass request context to serializer."""
        return {'request': self.request}


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class = PostModelFilter
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        """Pass request context to serializer."""
        return {'request': self.request}

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset = ['text']
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        """Pass request context to serializer."""
        return {'request': self.request}

class CommentLikeViewSet(viewsets.ModelViewSet):
    queryset = LikeComment.objects.all()
    serializer_class = serializers.LikeCommentSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset = ['text']
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        """Pass request context to serializer."""
        return {'request': self.request}

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'comment-likes', CommentLikeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
