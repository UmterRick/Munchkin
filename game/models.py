from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    myid = models.CharField(max_length=20, unique=True)
    status = models.IntegerField()

    def __str__(self):
        return self.myid


class Player(models.Model):
    game = models.ForeignKey(Game, models.CASCADE, 'player')
    level = models.PositiveIntegerField()
    myid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=15)
    p_class = models.CharField(max_length=30)
    p_race = models.CharField(max_length=30)
    power = models.IntegerField()
    status = models.IntegerField()
    temp_power = models.IntegerField()
    
    def __str__(self):
        return {'name':self.name,
                'id': self.myid,
                'status': self.status
                }
    
