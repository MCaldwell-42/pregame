from django.db import models
from django.contrib.auth.models import User


class UserEvent(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("UserEvent")
        verbose_name_plural = ("UserEvents")
