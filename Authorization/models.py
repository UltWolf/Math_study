from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank = True)
    picture = models.ImageField(upload_to='profile_images', blank=True,default="profile_images/no_avatar.png")
    school = models.CharField(max_length=60,blank= True)


    def __str__(self):
     return self.user.username