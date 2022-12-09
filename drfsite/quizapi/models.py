from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):

    header = models.TextField()
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.header
