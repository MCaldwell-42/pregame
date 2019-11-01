import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from pregameApp.models import Pregame, PregameNote, model_factory
from ..connection import Connection

def add_rsvp(request, pregame_id):
    if request.method == 'POST':

        form_data = request.POST
        with sqlite3.connect(Connection.db_path) as conn:
            current_user = request.user
            current_pregame = pregame_id

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