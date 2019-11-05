import sqlite3
from django.shortcuts import render, redirect, reverse
from pregameApp.models import Event
from pregameApp.models import model_factory
from django.contrib.auth.decorators import login_required
from ..connection import Connection
import googlemaps
from ..maps import Mapkey

def get_events():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Event)
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
        """)
        return db_cursor.fetchall()

@login_required
def event_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Event)
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
            """)

            all_events = db_cursor.fetchall()

        template = 'events/events_list.html'
        context = {
            'events': all_events
        }

        return render(request, template, context)

    elif request.method == 'POST':

        form_data = request.POST
        with sqlite3.connect(Connection.db_path) as conn:
            gmaps = googlemaps.Client(key=Mapkey)
            geocode_result = gmaps.geocode(form_data['address'])[0]
            event_lat = geocode_result['geometry']['location']['lat']
            event_long = geocode_result['geometry']['location']['lng']
            current_user = request.user

            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO pregameApp_event
            (
                name, address, description,
                date, time, img_url, latitude, longitude, created_by_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (form_data['name'], form_data['address'],
                form_data['description'], form_data['date'],
                form_data['time'], form_data['img_url'], event_lat, event_long, current_user.id ))

        return redirect(reverse('pregameApp:events'))


@login_required
def city_event_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            city = request.GET['search']
            conn.row_factory = model_factory(Event)
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
            where e.address like ?
            """, (f'%{city}%',))

            all_events = db_cursor.fetchall()

        template = 'events/events_list.html'
        context = {
            'events': all_events
        }

        return render(request, template, context)
