from django.db import models
from django.contrib.auth.models import AbstractUser 



# Create your models here.

class Person(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    number = models.CharField(max_length=20)
    skill = models.CharField(max_length=255)
    image = models.ImageField(upload_to='person_images/')

    def __str__(self): 
        return self.full_name
   
# this is model of skill


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=20, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
    image = models.ImageField(upload_to='skills/')

    def __str__(self):
        return self.name   
     
    
    
# this is model add for project 
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='projects/files/')
    image_file = models.ImageField(upload_to='projects/images/')
    
    def __str__(self):
        return self.name 
    
    
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/images/', blank=True, null=True)
    video = models.FileField(upload_to='blogs/videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    
class ClientService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='services/images/', blank=False, null=False)

    def __str__(self):
        return self.name 
    
    
    
