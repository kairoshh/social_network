from rest_framework import serializers

from apps.posts.models import Post, Like, DisLike


class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = (
            'id', 'title',
            'created_at',
            'image',
            'like_amount', 'dislike_amount',
        )
        read_only_fields = (
            'user',
        )

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'id', 
            'created_at',
            'user','title'
            
            )
        read_only_fields = (
            'id', 
            'created_at',
            'user','title',
            
            )

class DisLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisLike
        fields = (
            'id', 
            'created_at',
            'user','title',
          
            )
        
        read_only_fields = (
            'id', 
            'created_at',
            'user','title', 
            
        )

        


