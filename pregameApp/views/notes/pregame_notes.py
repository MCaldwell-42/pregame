import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from pregameApp.models import Pregame, PregameNote, model_factory
from ..connection import Connection
# Creates a new comment object for display on the pregame details page
@login_required
def post_pregame_notes(request, pregame_id):
    if request.method == 'POST':
        form_data = request.POST
        with sqlite3.connect(Connection.db_path) as conn:
            current_user = request.user
            current_pregame = pregame_id

            db_cursor = conn.cursor()       

            db_cursor.execute("""
            INSERT INTO pregameApp_pregamenote
            (
                note, user_id, pregame_id
            )
            VALUES (?, ?, ?)
            """,
            (form_data['note'], current_user.id, current_pregame ))

        return redirect(reverse('pregameApp:pregame_details', args=(pregame_id,)))

# deletes and edits pregame notes based on the button hit with some javascript magic.
def delete_pregame_note(request, note_id, pregame_id):
    if request.method == 'POST':
            form_data = request.POST

            if (
                "actual_method" in form_data
                and form_data["actual_method"] == "DELETE"
            ):
                with sqlite3.connect(Connection.db_path) as conn:
                    db_cursor = conn.cursor()

                    db_cursor.execute("""
                    DELETE FROM pregameApp_pregamenote
                    WHERE id = ?
                    """, (note_id,))

                return redirect(reverse('pregameApp:pregame_details', args=(pregame_id,)))
            elif (
                "actual_method" in form_data
                and form_data["actual_method"] == "EDIT"
            ):
                with sqlite3.connect(Connection.db_path) as conn:
                    db_cursor = conn.cursor()

                    db_cursor.execute("""
                    UPDATE pregameApp_pregamenote
                    SET note =?
                    WHERE id = ?
                    """, (form_data['note_content'], note_id,))

                return redirect(reverse('pregameApp:pregame_details', args=(pregame_id,)))