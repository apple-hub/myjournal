from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Journal(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    created_datetime = models.DateTimeField(default=timezone.now)
    updated_datetime = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.updated_datetime = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    journal = models.ForeignKey('journals.Journal', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_datetime = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.text