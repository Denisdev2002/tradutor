from django.db import models

# Create your models here.

class Traducao(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    language = models.CharField(max_length=2, blank=True, default='')
    target_language = models.CharField(max_length=2, default='')
    class Meta:
        ordering = ['created']