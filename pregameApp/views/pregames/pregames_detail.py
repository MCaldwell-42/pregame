import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from pregameApp.models import Pregame
from ..connection import Connection


def get_pregame(pregame_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
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

        template = 'pregame/pregame_detail.html'
        context = {
            'pregame': pregame,
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