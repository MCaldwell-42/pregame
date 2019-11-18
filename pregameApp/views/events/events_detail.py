import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from pregameApp.models import Event
from ..maps import Mapkey
from ..connection import Connection

# Retrieves and makes an event to display an event's details
def get_event(event_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            e.id,
            e.name,
            e.address,
            e.description,
            e.date,
            e.time,
            e.img_url,
            e.latitude,
            e.longitude,
            e.created_by_id
        from pregameApp_event e
        WHERE e.id = ?
        """, (event_id,))

        return db_cursor.fetchone()
# Get's the event and it's details and displays them on the given template
def event_details(request, event_id):
    if request.method == 'GET':
        event = get_event(event_id)

        template = 'events/event_detail.html'
        context = {
            'event': event,
            'Mapkey': Mapkey
        }

        return render(request, template, context)
