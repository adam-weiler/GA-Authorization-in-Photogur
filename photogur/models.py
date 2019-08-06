from django.contrib.auth.models import User
from django.db import models


class Picture(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'title={self.title}, artist={self.artist}, url={self.url}'
        return f'<img src=\'{self.url}\' alt=\'{self.title}\' />'


class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'\'{self.message}\' - {self.name}'

