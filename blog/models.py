from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User')
    content = models.TextField()
    created_date = models.DateField(default=timezone.now)

    is_published = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering=['-created_date']

    @property
    def approved_replies(self):
        return self.replies.filter(approved_reply=True)

    def publish(self):
        self.is_published = True
        self.save()

    def unpublish(self):
        self.is_published = False
        self.save()

    def delete(self):
        self.is_deleted = True
        self.save()


class Reply(models.Model):
    post = models.ForeignKey(Post, related_name='replies')
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    content = models.TextField()
    created_date = models.DateField(default=timezone.now)

    approved_reply = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def approve(self):
        self.approved_reply = True
        self.save()

    def delete(self):
        self.is_deleted = True
        self.save()
