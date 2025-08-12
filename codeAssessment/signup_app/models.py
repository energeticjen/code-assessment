from django.db import models

class User(models.Model):
    name = models.CharField(blank=False, max_length=255)
    age = models.IntegerField(null=True)
    title = models.CharField(blank=False, max_length=100)
    hometown = models.CharField(max_length=200)

    def __str__(self):
        return self.name
