# Generated by Django 2.1 on 2018-08-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='images',
            field=models.ImageField(blank=True, default='default_dog.png', upload_to='dog_images/<django.db.models.fields.CharField>'),
        ),
    ]
