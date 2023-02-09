from django.db import models

# Create your models here.


class FeedBack(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    feedback = models.TextField()
    rating = models.PositiveIntegerField()