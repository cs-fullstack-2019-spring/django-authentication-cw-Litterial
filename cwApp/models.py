from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class FoodFitness(models.Model):
    username=models.CharField(max_length=900, default='')
    calories=models.PositiveIntegerField()
    date=models.DateField(default='')
    password=models.CharField(max_length=900, default='')
    userTableForeignKey = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.username
