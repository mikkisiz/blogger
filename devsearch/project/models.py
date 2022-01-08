from django.db import models
from django.contrib.auth.models import User
import uuid
from users.models import Profile
from django.db.models.signals import post_save
# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profile, null = True, blank = True, on_delete=models.SET_NULL)
    title = models.CharField(max_length = 200)
    desciption = models.TextField(null = True, blank = True)
    demo_link = models.CharField(max_length = 2000, null = True, blank = True)
    featured_image = models.ImageField(null = True, blank = True, default = "default.jpg")
    source_link = models.CharField(max_length=2000, null = True, blank= True )
    tags = models.ManyToManyField('Tag', blank = True)
    vote_total = models.IntegerField(default = 0, null = True, blank = True)
    vote_ratio = models.IntegerField(default = 0, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable= False)
  
    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_Type = (
        ('up','Up vote'),
        ('down', 'Down vote')
    )
    #owner = 
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    body = models.TextField(null = True, blank = True)
    value = models.CharField(max_length = 200, choices = VOTE_Type)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable= False)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)

    def __str__ (self):
        return self.name

def profileUpdated(sender, instance, created, **kwargs):
    print('profile saved!')


post_save.connect(profileUpdated, sender = Profile)
