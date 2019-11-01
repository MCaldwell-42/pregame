import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from pregameApp.models import Pregame, UserPregame, model_factory
from ..connection import Connection

def get_pregame_rsvps():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(UserPregame)
        db_cursor = conn.cursor()
        db_cursor.execute("""
        select
            rsvp.id,
            rsvp.pregame_id,
            rsvp.user_id
            
        from pregameApp_userpregame rsvp
        """)
        return db_cursor.fetchall()


def add_rsvp(request, pregame_id):
    if request.method == 'POST':
        unique_rsvps = get_pregame_rsvps()
        current_user = request.user
        current_pregame = pregame_id
        for vps in unique_rsvps:
            if vps.user_id != current_user.id and vps.pregame_id != current_pregame:
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