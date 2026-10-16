from django.shortcuts import render

from .serializers import PostSerializer
from .models import Post
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer