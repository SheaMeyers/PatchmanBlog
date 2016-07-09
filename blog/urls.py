from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^reply/(?P<pk>\d+)/approve/$', views.reply_approve, name='reply_approve'),
    url(r'^reply/(?P<pk>\d+)/remove/$', views.reply_remove, name='reply_remove'),
]