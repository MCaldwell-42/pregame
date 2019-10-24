from django.db import models
from django.contrib.auth.models import User

class UserPregame(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pregame = models.ForeignKey("Pregame", on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("UserPregame")
        verbose_name_plural = ("UserPregames")
