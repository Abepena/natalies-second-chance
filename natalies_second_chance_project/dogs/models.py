from django.db import models
from django.urls import reverse
# Create your models here.

class Dog(models.Model):
    # Size choices
    SMALL = "SM"
    MEDIUM = "MD"
    LARGE = "LG"
    EXTRA_LARGE = "XL"
    DOG_SIZE_CHOICES = (
        (SMALL, "Small (Under 10 lbs)" ),
        (MEDIUM, "Medium (10 to 40 lbs)" ),
        (LARGE, "Large (40 to 100 lbs)" ),
        (EXTRA_LARGE, "X-Large (Over 100 lbs)" ),
    )

    #Sex Choices
    MALE = 'M'
    FEMALE = 'F'
    DOG_SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='dog_images/', default="default_dog.png")
    size = models.CharField(max_length=2, choices=DOG_SIZE_CHOICES)
    sex = models.CharField(max_length=1, )

    def get_absolute_url(self):
        return reverse('dogs:detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = ('Dog')
        verbose_name_plural = ('Dogs')
        ordering = ('-pk',)
    
    def __str__(self):
        return self.name