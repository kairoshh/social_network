from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from apps.posts.serializers import  PostSerializer, LikeSerializer, DisLikeSerializer

from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from apps.posts.models import Post, Like, DisLike

User = get_user_model()

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action


        

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly, )
    # filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter )
    search_fields = (
        'title', 'user__username',
    )
    filterset_fields = (
        'is_draft',
    )
    ordering_fields = (
        'created_at',
    )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'add_like':
            return LikeSerializer
        elif self.action == 'add_dislike':
            return DisLikeSerializer
        else:
            return PostSerializer
    

    @action(methods=['post',], detail=True)
    def add_like(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        like = Like.objects.filter(title = post, user=user)
        dislike = DisLike.objects.filter(title=post, user=user)
        if like.exists():
            like.delete()
            return Response({
                'like was delted'})
        elif dislike.exists():
            dislike.delete()
            Like.objects.create(user=user, title=post)
            return Response({
                'dislike was deleted, like was add'
            })
        else:
            Like.objects.create(title=post, user=user)
            return Response({
              'like created'  
            })

    @action(methods=['post',], detail=True)
    def add_dislike(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        like = Like.objects.filter(title = post, user=user)
        dislike = DisLike.objects.filter(title = post, user=user)
        if dislike.exists():
            dislike.delete()
            return Response({
                'dislike was delted'})
        elif like.exists():
            like.delete()
            Like.objects.create(user=user, title=post)
            return Response({
                'like was deleted, dislike was add'
            })
        else:
            DisLike.objects.create(title=post, user=user)
            return Response({
              'dislike created'  
            })



