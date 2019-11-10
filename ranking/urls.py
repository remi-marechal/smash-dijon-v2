from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate-tournament', views.update_with_smashgg, name='calculate-tournament'),
    path('reset-tournament', views.reset_state_tournament, name='reset-tournament'),
    path('tournaments-manage', views.tournament_manage, name='tnmanage'),
    path('vods-admin', views.vods_manage, name='vodsmanage'),
    path('login', views.connexion, name='login'),
    path('logout', views.deconnexion, name='logout'),
    path('about', views.about, name='about'),
    path('vod', views.vod, name='vod'),
    path('vod/<str:tn_name_slug>', views.vod_by_tournament, name='vod_by_tn'),
    path('test', views.test_youtube, name='test'),
    path('tournaments', views.tournament_list, name='tnlist'),
    path('players', views.player_list, name='playerlist'),
    path('players/<str:player_name>', views.player_info, name='playerinfo'),
    path('authorize', views.authorize, name='authorize'),
    path('oauth2callback', views.oauth2callback, name='oauth'),
]