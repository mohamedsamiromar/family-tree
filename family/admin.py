from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Person)
admin.site.register(Father)
admin.site.register(Mather)
admin.site.register(GrandFather)
admin.site.register(GrandMother)
admin.site.register(GreatGrandFather)
admin.site.register(GreatGrandMother)