# Generated by Django 2.1 on 2018-08-28 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0002_auto_20180826_1849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dog',
            options={'ordering': ('-pk',), 'verbose_name': 'Dog', 'verbose_name_plural': 'Dogs'},
        ),
        migrations.AddField(
            model_name='dog',
            name='size',
            field=models.CharField(choices=[('SM', 'Small (Under 10 lbs)'), ('MD', 'Medium (10 to 40 lbs)'), ('LG', 'Large (40 to 100 lbs)'), ('XL', 'X-Large (Over 100 lbs)')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='images',
            field=models.ImageField(blank=True, default='default_dog.png', null=True, upload_to='dog_images/<django.db.models.fields.CharField>'),
        ),
    ]
