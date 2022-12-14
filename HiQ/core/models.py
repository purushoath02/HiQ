from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class profile(models.Model): 
    user: models.ForeignKey(User, on_delete=models.CASCADE)
    id_user: models.IntegerField()
    profile_img = models.ImageField(upload_to='profile_img', default='default/profile.png')
    bio = models.TextField(max_length=500, blank=True)
    def __str__(self): 
        return self.user.username
     