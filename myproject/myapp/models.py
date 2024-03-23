from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1337)


class Human(models.Model):
    name = models.TextField()
    surname = models.TextField()
    birthdate = models.DateField()