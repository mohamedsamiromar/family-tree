from django.contrib import admin
from .models import *


# class PersoneAdmin(admin.ModelAdmin):
#     model = Person
#     list_filter = '__all__'

# Register your models here.
admin.site.register(Person)
