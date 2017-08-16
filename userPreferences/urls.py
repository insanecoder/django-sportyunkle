from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.registerUser, name='register/register_user'),
]