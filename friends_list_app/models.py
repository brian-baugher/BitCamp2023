from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserFriends(models.Model):
    user = models.CharField(max_length = 200, null=True)
    friend = models.CharField(max_length = 200)