from django.db import models
from coachme.users.models import User


class Goal(models.Model):

    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Step(models.Model):

    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField(default=1)
    done = models.BooleanField(default=False)
    points = models.PositiveIntegerField(default=0)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
