from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.conf import settings

# Create your models here.
class Bio(models.Model):
    #Brian Rafferty's Portfolio
    title = models.CharField(max_length=100)
    #Who am I?
    description = models.TextField()
    #My profile picture
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #Objective, where i want to go with my career
    objective = models.TextField()
    #College name -- degree earned -- year graduated
    education = models.TextField()

class Project(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.TextField()
    image = models.ImageField(default='default_project.jpg', upload_to='project_pics')
    gitRepo = models.TextField(default='webpage.com')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})