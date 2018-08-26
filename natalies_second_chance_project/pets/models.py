from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_page_count(self):
        pass
    
class DogImage(models.Model):
    dog = models.ForeignKey(Dog, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()