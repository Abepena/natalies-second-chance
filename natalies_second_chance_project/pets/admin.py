from django.contrib import admin
from .models import Dog, DogImage
# Register your models here.

class DogImageInline(admin.TabularInline):
    model = DogImage
    extra = 3

class DogAdmin(admin.ModelAdmin):
    inline = ['DogImageInline',]

admin.site.register(Dog)



