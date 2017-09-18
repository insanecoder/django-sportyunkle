from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addBlog/(?P<pk>\d*)$', views.add_blog, name='add_blog'),
    url(r'^saveBlog$', views.save_blog, name='save_blog'),
]