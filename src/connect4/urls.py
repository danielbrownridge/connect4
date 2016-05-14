from django.conf.urls import url

from . import views

app_name = 'connect4'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup$', views.signup, name='signup'),
]
