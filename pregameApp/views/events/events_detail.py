import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from pregameApp.models import Event
# from pregameApp.views import get_pregames
from ..connection import Connection


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

@login_required # remove before launch for events only
def event_details(request, event_id):
    if request.method == 'GET':
        event = get_event(event_id)
        # all_pregames = get_pregames()

        template = 'events/event_detail.html'
        context = {
            'event': event,
            # 'all_pregames': all_pregames
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
    #             DELETE FROM pregameApp_event
    #             WHERE id = ?
    #             """, (event_id,))

    #         return redirect(reverse('pregameApp:event'))