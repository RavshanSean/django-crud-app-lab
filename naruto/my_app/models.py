from django.db import models
from django.urls import reverse


    # Add the Weapon model
class Weapon(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('weapon-detail', kwargs={'pk': self.id})


# Create your models here.
class Ninja(models.Model):
    name = models.CharField(max_length=100)
    clan = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    weapon = models.ManyToManyField(Weapon)
    chakra = models.CharField()


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ninja-detail', kwargs={'ninja_id': self.id})