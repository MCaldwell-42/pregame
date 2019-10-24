from django.db import models
from django.contrib.auth.models import User
from .event import Event

class EventNote(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    note = models.CharField(max_length=1500)
    

    class Meta:
        verbose_name = ("EventNote")
        verbose_name_plural = ("EventNotes")

