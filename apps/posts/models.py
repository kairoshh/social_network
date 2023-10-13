from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='post/images')
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name='posts'
    )

    @property
    def like_amount(self):
        return self.likes.count()

    @property
    def dislike_amount(self):
        return self.dislikes.count()

class Like(models.Model):
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
    to=User, on_delete=models.CASCADE,
    related_name='likes'
    )
    title = models.ForeignKey(
    to=Post, on_delete=models.CASCADE,
    related_name='likes'
    )

class DisLike(models.Model):
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
    to=User, on_delete=models.CASCADE,
    related_name='dislikes'
    )
    title = models.ForeignKey(
    to=Post, on_delete=models.CASCADE,
    related_name='dislikes'
    )

    


