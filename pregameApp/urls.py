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
    # path('events/<int:event_id>/', event_details, name='event'),
    # path('pregames/', pregame_list, name='pregame_list'),
    # path('pregame/form', pregame_form, name='pregame_form'),
    # path('pregames/<int:pregame_id>', pregame_details, name='pregame'),
    # path('pregames/', pregame_list, name='pregame_list'),

]
