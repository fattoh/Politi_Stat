"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Statments(models.Model):
    statment = models.CharField(max_length=1000, default='SOME STRING')
    Paragraph = models.CharField(max_length=1000, default='SOME STRING')

class User_Rates(models.Model):
    userRate_id = models.CharField(max_length=100,default='SOME STRING')
    rates = models.CharField(max_length=1000, default='SOME STRING')
    qustions = models.CharField(max_length=1000, default='SOME STRING')
