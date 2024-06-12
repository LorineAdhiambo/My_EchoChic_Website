from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/')

class Milestone(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField()
