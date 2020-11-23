from django.db import models

# Create your models here.
class ContentPiece(models.Model):
    quantity=models.IntegerField(default=1)
    author=models.CharField(max_length=100, default="Who did it?")
    title=models.CharField(max_length=200, default="what was it?")
    note=models.TextField()
    week=models.IntegerField(default=1)
    published=models.BooleanField(default=True)

class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    published=models.BooleanField(default=True)
