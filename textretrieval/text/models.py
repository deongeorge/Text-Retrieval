from django.db import models

# Create your models here.
class Text(models.Model):
    title = models.CharField(max_length=100,null = True)
    snippet = models.CharField(max_length=300, null=True)