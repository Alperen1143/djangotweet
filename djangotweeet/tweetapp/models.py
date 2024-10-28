from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User



# Create your models here.

class Tweet(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    message = models.CharField(max_length=100)

    def __str__(self):
        return f"Tweet user:{self.username},Tweet Message: {self.message}"

