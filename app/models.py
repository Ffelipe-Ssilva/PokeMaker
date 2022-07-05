from ast import type_ignore
from unicodedata import name
from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    typeOne= models.CharField(max_length=30)
    typeTwo= models.CharField(max_length=30)
    hp= models.IntegerField()
    attack=models.IntegerField()
    defense= models.IntegerField()
    spAttack= models.IntegerField()
    spDefense= models.IntegerField()
    speed=models.IntegerField()




