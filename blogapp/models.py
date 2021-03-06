import profile
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date




# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField(max_length=300,default="s1mple")
    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=300)
    pic = models.ImageField(null=True , blank= True , upload_to = 'images/')
    title_tag = models.CharField(max_length=300,default="s1mple")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    post_date=models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' +str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')