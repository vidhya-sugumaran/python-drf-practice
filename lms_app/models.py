from django.db import models


class LMS(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
