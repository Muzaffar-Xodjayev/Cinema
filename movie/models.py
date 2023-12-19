from django.db import models

# Create your models here.


class Category(models.Model):
    """ Category """
    name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    """ Actor """
    name = models.CharField(max_length=255)
    birt_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to="actors/")

    def __str__(self):
        return self.name


class Genre(models.Model):
    """ Genres """
    name = models.CharField(max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=155, unique=True)

    def __str__(self):
        return self.name

