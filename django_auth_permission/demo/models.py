from django.db import models


# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=128)
