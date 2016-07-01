from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User')
    created_date = models.DateField(default=timezone.now)
    content = models.TextField()

    is_published = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering=['-created_date']

    def publish(self):
        self.save()