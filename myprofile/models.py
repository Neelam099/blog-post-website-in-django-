from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="img", blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    
    @property
    def profile_pic(self):
        if self.pic == "":
            self.pic = ""
        return self.pic

    
    def __str__(self):
        return self.user.username
    
    
    



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, 
                username=instance.username, email=instance.email)
        
        

@receiver(post_save, sender=UserProfile)
def update_user(sender, instance, **kwargs):
    
    user = instance.user
    user.username = instance.username
    user.email = instance.email
    user.first_name = instance.first_name
    user.last_name = instance.last_name
    
    
    user.save()
  
