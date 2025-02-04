from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
