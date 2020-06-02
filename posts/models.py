from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
