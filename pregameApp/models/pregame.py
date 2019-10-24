from django.db import models
from django.contrib.auth.models import User
from .event import Event
from .user_pregame import UserPregame

class Pregame(models.Model):

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    img_url = models.URLField(max_length=200, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    

    class Meta:
        verbose_name = ("Pregame")
        verbose_name_plural = ("Pregames")

    @property
    def total_RSVP(self):
        return UserPregame.objects.filter(pregame=self).count()
