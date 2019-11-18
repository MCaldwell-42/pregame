import sqlite3
from django.shortcuts import render, redirect, reverse
from pregameApp.models import Event
from pregameApp.models import model_factory
from django.contrib.auth.decorators import login_required
from ..connection import Connection
import googlemaps

# gets the form to add a new event
@login_required
def event_form(request):
    if request.method == 'GET':
        template = 'events/events_form.html'

        return render(request, template)