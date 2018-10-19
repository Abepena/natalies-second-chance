import os
import django
import random

# set the environment settings before manipulating the actual models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'natalies_second_chance.settings')
django.setup()

#Fake population script
from dogs.models import Dog
from faker import Faker

fake = Faker()

SIZE_CHOICES = ['SM', 'MD', 'LG', 'XL']
SEX_CHOICES = ['M', 'F']

def add_dog(n=5):

    for i in range(n):
        # Populate all the fields in the Dog model (the image will be the default image)
        name = fake.first_name()
        breed = fake.word().capitalize()
        age = random.randint(0,10)
        description = fake.text(max_nb_chars=400)
        size = random.choice(SIZE_CHOICES)
        sex = random.choice(SEX_CHOICES)

        # Returns a tuple of if the instance and boolean whether it was created or it existed
        # we only need the first value of the tuple
        dog = Dog.objects.get_or_create(
            name=name,
            breed=breed, 
            age=age, 
            description=description,
            size=size,
            sex=sex,
        )[0]
        print(f'adding {dog.name} to the database')
        dog.save()

if __name__ == "__main__":
    print('populating database')
    add_dog(9)
    print('Populating Done')
