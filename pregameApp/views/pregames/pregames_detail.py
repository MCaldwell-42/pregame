import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from pregameApp.models import Pregame, PregameNote, model_factory
from ..connection import Connection


def get_pregame_notes(pregame_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(PregameNote)
        db_cursor = conn.cursor()
        db_cursor.execute("""
        select
            n.id,
            n.note,
            n.pregame_id,
            n.user_id,
            u.username
        from pregameApp_pregamenote n
        join auth_user u on n.user_id = u.id
        where n.pregame_id = ?
        """, (pregame_id,))
        return db_cursor.fetchall()

def get_pregame(pregame_id):
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
        WHERE p.id = ?
        """, (pregame_id,))

        return db_cursor.fetchone()

@login_required
def pregame_details(request, pregame_id):
    if request.method == 'GET':
        pregame = get_pregame(pregame_id)
        notes = get_pregame_notes(pregame_id)
        user_id = request.user.id

        template = 'pregame/pregame_detail.html'
        context = {
            'pregame': pregame,
            'notes': notes,
            'pregame_id': pregame_id,
            'user_id': user_id
        }

        return render(request, template, context)

    # delete if needed later
    # if request.method == 'POST':
    #     form_data = request.POST

    #     if (
    #         "actual_method" in form_data
    #         and form_data["actual_method"] == "DELETE"
    #     ):
    #         with sqlite3.connect(Connection.db_path) as conn:
    #             db_cursor = conn.cursor()

    #             db_cursor.execute("""
    #             DELETE FROM pregameApp_pregame
    #             WHERE id = ?
    #             """, (event_id,))

    #         return redirect(reverse('pregameApp:pregame'))