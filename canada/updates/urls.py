from django.conf.urls.defaults import patterns, include, url
from canada.updates.views import UpdateListView

urlpatterns = patterns('',
    url(r'^$', UpdateListView.as_view(), name='updates_list'),
    )
