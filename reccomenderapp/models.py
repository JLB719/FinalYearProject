from django.db import models


# Create your models here.
class UserPreferences(models.Model):
    """
    Model definiton for storing user preferences
    """
    username = models.TextField(default='')
    maxyear = models.IntegerField(default=0)
    numberofepisodes = models.IntegerField(default=0)
    languages = models.TextField(default='')
    origincountries = models.TextField(default='')
    likedgenres = models.TextField(default='')
    dislikedgenres = models.TextField(default='')
    likedshows = models.TextField(default='')
    dislikedshows = models.TextField(default='')
