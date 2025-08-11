from django.contrib.auth.models import User
from django.db import models
from datetime import timedelta


class Actor(models.Model):
    class GENDER(models.TextChoices):
        MALE = 'male', 'male'
        FEMALE = 'female', 'female'

    name = models.CharField(max_length=255)
    country = models.CharField(max_length=80, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER.choices)
    birthdate = models.DateField(blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.SmallIntegerField(blank=True, null=True)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    duration = models.DurationField(default=timedelta(days=30))

    def __str__(self):
        return self.name

class Review(models.Model):
    comment = models.TextField()
    rate = models.SmallIntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:40]


