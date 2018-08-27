from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    description = models.TextField()
    images = models.ImageField(upload_to=f'dog_images/{name}',blank=True, default="default_dog.png")

    def __str__(self):
        return self.name

    def has_multiple_images(self):
        return self.images.count() > 1