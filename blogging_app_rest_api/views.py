from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from rest_framework import generics
from blogging_app_rest_api import views
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_staff', 'email']
