from django.db import models


# Create your models here.
class StudentModel(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    age = models.IntegerField(max_length=3)

    def __str__(self):
        return self.fname
