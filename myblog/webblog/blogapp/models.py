from time import timezone
from django.db import models

# Create your models here.
class Post(models.Model) :
    province = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200)
    publishDate = models.CharField(max_length=80, null=True)
    body = models.TextField()

    def __str__(self) :
        return self.title

