from django.urls import path
from django.conf.urls import include, url
from pregameApp import views
from .views import *

app_name = 'pregameApp'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('events/', event_list, name='events'),
    path('events/form/', event_form, name='event_form'),
    path('events/<int:event_id>/', event_details, name='event'),
    path('pregames/<int:event_id>', pregame_list, name='pregame'),
    path('pregames/form/<int:event_id>', pregame_form, name='pregame_form'),
    path('pregames/details/<int:pregame_id>', pregame_details, name='pregame_details'),
    path('comment/<int:pregame_id>', post_pregame_notes, name='post_pregame_notes'),
    path('delete/<int:pregame_id>/<int:note_id>', delete_pregame_note, name='delete_pregame_note'),
    path('pregames/rsvp/<int:pregame_id>', add_rsvp, name='pregame_rsvp'),

]
