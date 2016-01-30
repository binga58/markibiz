from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=128,blank=False,null=False)
    description = models.TextField()
    oraganizer = models.ForeignKey('Team')

    prize = models.IntegerField()
    poster = models.ImageField(upload_to='event_img/',null=True)
    registration_start = models.DateTimeField()
    registration_end =models.DateTimeField()
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    active = models.BooleanField()
    sponsor = models.CharField(max_length=128,blank=True,null=True)
    registration_link = models.URLField()
    speaker = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=128,blank=False,null=False)
    email_id = models.EmailField(blank=False,null=False)

class Feedback(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(blank=False,null=False)
    message = models.TextField(blank=False,null=False)


class Team(models.Model):
    LEVEL = (
        ('JUNIOR', 'JUNIOR'),
        ('SENIOR', 'SENIOR'),
    )
    name = models.CharField(max_length=128)
    about = models.TextField(null=True,blank=True)
    post = models.CharField(max_length=128)
    image = models.ImageField(upload_to='team_img/',null=True)
    email = models.EmailField()
    mobile = models.IntegerField()
    level = models.CharField(max_length=6,choices=LEVEL)

    def __str__(self):
        return self.name
