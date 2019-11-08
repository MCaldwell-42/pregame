import sqlite3
from django.shortcuts import render, redirect, reverse
from pregameApp.models import Pregame
from pregameApp.models import model_factory
from django.contrib.auth.decorators import login_required
from ..connection import Connection
import googlemaps

# gets form for creating a new pregame
@login_required
def pregame_form(request, event_id):
    if request.method == 'GET':
        template = 'pregame/pregame_form.html'
        context = {
            'event_id': event_id
        }

        return render(request, template, context)