from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

#Creating a model for the Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #Creating an author field which will be based on the user logged in
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, unique= False, null=False, related_name='author')
    #Image
    header_image = models.ImageField(null = True, blank=True, upload_to='media/image')
    #Like field and using many to many so that a user can have likes on multiple posts
    liked = models.ManyToManyField(User, related_name='likes', blank=True, default= None)
    #Field for the number of likes
    num_likes = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.title

    #Defining a funtion that returns the number of likes
    @property
    def num_likes(self):
        return self.liked.all().count()



