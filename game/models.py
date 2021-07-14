from django.db import models
from django.contrib.auth.models import User
import uuid


class Game(models.Model):
    myid = models.CharField(primary_key=True,max_length=40)
    status = models.IntegerField()

    def __str__(self):
        return str(self.myid)


class Player(models.Model):
    game = models.ForeignKey(Game, models.CASCADE, 'player')
    myid = models.CharField(primary_key=True, default=str(uuid.uuid4()), max_length=40)

    name = models.CharField(max_length=15)

    p_class = models.CharField(max_length=30, default='Human')
    s_class = models.CharField(max_length=30, null=True)

    p_race = models.CharField(max_length=30, default='Human')
    s_race = models.CharField(max_length=30, null=True)

    level = models.PositiveIntegerField(default=1)
    power = models.IntegerField(default=0)
    temp_power = models.IntegerField(default=0)

    status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name
