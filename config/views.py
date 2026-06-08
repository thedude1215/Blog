from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'])
    def related(self, request, pk=None):
        post = self.get_object()
        
        # Make sure the post actually has a category before filtering
        if post.category:
            related = Post.objects.filter(category=post.category).exclude(id=post.id)[:7]
        else:
            related = Post.objects.none()
            
        # Serialize the queryset so it can be returned as JSON
        serializer = self.get_serializer(related, many=True)
        return Response(serializer.data)

class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
