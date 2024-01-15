from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    car_name =  models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

class Post(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.FileField(upload_to='images/',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='post_thumbnails/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    def like_count(self):
        return Like.objects.filter(post=self).count()
    
    def show_logo(self):
        return format_html('<img src="/static/%s" width="100" />' %
        self.image)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(default='0.0.0.0')

    class Meta:
        unique_together = ('user', 'post')  # Ensure a user can only like a post once

    def __str__(self):
        return f'{self.user.username if self.user else "Anonymous"} likes {self.post.name}'

class Comment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()