from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField(max_length=1200)

    def __str__(self):
        return self.title
