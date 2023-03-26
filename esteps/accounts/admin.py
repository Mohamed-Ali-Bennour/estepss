from django.contrib import admin
from .models import  Profile , Locations,Permission_level
# Register your models here.


admin.site.register(Profile)
admin.site.register(Locations)
admin.site.register(Permission_level)
