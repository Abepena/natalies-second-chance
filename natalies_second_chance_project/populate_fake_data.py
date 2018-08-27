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

def add_dog(n=5):

    for i in range(n):
        name = fake.first_name()
        breed = fake.word().capitalize()
        age = random.randint(1,10)
        description = fake.text(max_nb_chars=400)

        dog = Dog.objects.get_or_create(name=name, breed=breed, age=age, description=description)[0]
        print(f'adding {dog.name} to the database')
        dog.save()

if __name__ == "__main__":
    print('populating database')
    add_dog(10)
    print('Populating Done')
