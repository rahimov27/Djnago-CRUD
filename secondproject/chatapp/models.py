from django.db import models


# Create your models here.
class MessageModel(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.username
