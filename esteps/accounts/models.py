from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    role = models.CharField(max_length=50)
    is_online = models.BooleanField(default=False)
    phone_number=models.CharField(max_length=50,default="test")
    job_locatin=models.CharField(max_length=50,default="test")
    def __str__(self):
        return  self.user.username

class Permission_level(models.Model):

    profile_from=models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='profile1')
    profile_to=models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='profile2')
    Permission_level=models.IntegerField(default=1)





class Locations (models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='location')


    latitude = models.FloatField()
    longitude = models.FloatField()


