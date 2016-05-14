from django.conf.urls import url

from . import views

app_name = 'connect4'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^signup$', views.SignupView.as_view(), name='signup'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
]
