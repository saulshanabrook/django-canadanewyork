from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView

from .views import ExhibitionDetailPress
from .models import Exhibition


urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Exhibition)),
    url(r'^(?P<year>\d{4})/(?P<slug>[-\w]+)/(?P<press>(press)|)$',
        ExhibitionDetailPress.as_view(),
        name='exhibition-detail'),
)
