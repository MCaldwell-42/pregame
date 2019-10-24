from django.db import models
from django.contrib.auth.models import User
from .pregame import Pregame

class PregameNote(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pregame = models.ForeignKey(Pregame, on_delete=models.CASCADE)
    note = models.CharField(max_length=1500)
    

    class Meta:
        verbose_name = ("PregameNote")
        verbose_name_plural = ("PregameNotes")
