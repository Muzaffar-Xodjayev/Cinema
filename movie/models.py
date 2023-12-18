from django.db import models

# Create your models here.


class Category(models.Model):
    """ Category """
    name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

