from django.conf.urls import include, url

from . import views

app_name = 'connect4'
urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^games/$', views.GamesView.as_view(), name='games'),
    url(r'^game/new/$', views.NewGameView.as_view(), name='game-new'),
    url(r'^game/(?P<game_id>[0-9]+)/data/$', views.GameDataView.as_view(), name='game-data'),
    url(r'^play/(?P<game_id>[0-9]+)/$', views.PlayView.as_view(), name='play'),
]
