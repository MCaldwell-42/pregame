import sqlite3
from django.shortcuts import render, redirect, reverse
from pregameApp.models import Pregame
from pregameApp.models import model_factory
from django.contrib.auth.decorators import login_required
from ..connection import Connection
import googlemaps
from ..maps import Mapkey

def get_pregames():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Pregame)
        db_cursor = conn.cursor()
        db_cursor.execute("""
        select
            p.id,
            p.name,
            p.address,
            p.description,
            p.date,
            p.time,
            p.img_url,
            p.latitude,
            p.longitude,
            p.created_by_id,
            p.event_id
        from pregameApp_pregame p
        """)
        return db_cursor.fetchall()
# gets all of the pregames for the given event and displays them on the given template
@login_required
def pregame_list(request, event_id):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Pregame)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
            p.id,
            p.name,
            p.address,
            p.description,
            p.date,
            p.time,
            p.img_url,
            p.latitude,
            p.longitude,
            p.created_by_id,
            p.event_id,
            e.name event_name,
            e.latitude event_lat,
            e.longitude event_long
            from pregameApp_pregame p
            join pregameApp_event e on p.event_id = e.id
            WHERE p.event_id = ?
            """, (event_id,))

            all_event_pregames = db_cursor.fetchall()

        template = 'pregame/pregame_list.html'
        context = {
            'pregames': all_event_pregames,
            'event_id': event_id,
            'Mapkey': Mapkey
        }

        return render(request, template, context)
# When posting a new pregame, the address in your data form is used to query googlemaps api
# to get the coordinates that are put into the object upon creation.  
    elif request.method == 'POST':

        form_data = request.POST
        with sqlite3.connect(Connection.db_path) as conn:
            gmaps = googlemaps.Client(key=Mapkey)
            geocode_result = gmaps.geocode(form_data['address'])[0]
            event_lat = geocode_result['geometry']['location']['lat']
            event_long = geocode_result['geometry']['location']['lng']
            current_user = request.user
            current_event = event_id

            db_cursor = conn.cursor()       

            db_cursor.execute("""
            INSERT INTO pregameApp_pregame
            (
                name, address, description,
                date, time, img_url, latitude, longitude, created_by_id, event_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (form_data['name'], form_data['address'],
                form_data['description'], form_data['date'],
                form_data['time'], form_data['img_url'], event_lat, event_long, current_user.id, current_event ))

        return redirect(reverse('pregameApp:pregame', args=(event_id,)))
