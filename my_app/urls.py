from django.urls import re_path
from . import views

urlpatterns = [
 re_path(r'^ass1$', views.post_list, name='post_list'),
 re_path(r'^assortment/new/$', views.post_new, name='post_new'),
 re_path(r'^ass/$', views.pp, name='pp'),
 re_path(r'^$', views.start, name='start'),
]




