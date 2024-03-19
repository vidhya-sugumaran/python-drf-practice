from django.db import models

class Dictionary(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    avail_status = models.CharField(max_length=100)

    def __str__(self):
        return self.title
