from django.db import models
from django.contrib.auth.models import User
from myprofile.models import UserProfile




# Create your models here.
class BlogPost(models.Model):
    
    availabilty = (
                    ('DR', "Draft"),
                   ('PUB', "Published")
                   )
    writer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField()
    show = models.CharField(max_length=3, choices=availabilty)
    image = models.ImageField(upload_to='img', default= 'default.jpg', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.body


