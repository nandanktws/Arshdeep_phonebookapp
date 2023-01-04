from django.db import models

class Phonebook(models.Model):
    name = models.CharField(max_length = 100)
    contactnum= models.CharField(max_length = 100,null=True,unique=True)