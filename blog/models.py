from django.conf import settings
from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    """
    Description: Model Description
    """
    title = models.CharField("제목", max_length=50)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'id': self.id})
