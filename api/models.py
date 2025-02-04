from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who liked the comment
    comment = models.ForeignKey(Comment, related_name='comment_likes', on_delete=models.CASCADE)  # The comment that was liked
    created_at = models.DateTimeField(auto_now_add=True)

class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who liked the comment
    post = models.ForeignKey(Comment, related_name='post_likes', on_delete=models.CASCADE)  # The comment that was liked
    created_at = models.DateTimeField(auto_now_add=True)
