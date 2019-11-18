import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from pregameApp.models import Pregame, UserPregame, model_factory
from ..connection import Connection
# This attempts to get an rsvp by the current user for the current pregame. It is used as a check in the below function.
def get_user_rsvps(pregame_id, user_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(UserPregame)
        db_cursor = conn.cursor()
        db_cursor.execute("""
        select
            rsvp.id,
            rsvp.pregame_id,
            rsvp.user_id
            
        from pregameApp_userpregame rsvp
        where rsvp.pregame_id = ? and rsvp.user_id = ?
        """, (pregame_id, user_id,))

        return db_cursor.fetchall()

# When one clicks the RSVP button this function runs. It used to above fetch to see if an rsvp already exists.
# If it does, then the user may not add another rsvp. If not, then an rsvp is created in the join table. 
def add_rsvp(request, pregame_id):
    if request.method == 'POST':
        current_user = request.user
        current_pregame = pregame_id
        unique_rsvps = get_user_rsvps(current_pregame, current_user.id)
        if unique_rsvps:
            return redirect(reverse('pregameApp:pregame_details', args=(pregame_id,)))
        else:
            form_data = request.POST
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()       
                db_cursor.execute("""
                INSERT INTO pregameApp_userpregame
                (
                    pregame_id, user_id
                )
                VALUES (?, ?)
                """,
                (current_pregame, current_user.id))
                return redirect(reverse('pregameApp:pregame_details', args=(pregame_id,)))
