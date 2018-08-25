from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="dog_images/")

    def __str__(self):
        return self.name
