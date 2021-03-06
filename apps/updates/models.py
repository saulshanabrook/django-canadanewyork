from django.db import models
from django.core.urlresolvers import reverse

import url_tracker
import dumper
import simpleimages.trackers

from apps.photos.models import BasePhoto
from libs.ckeditor.fields import CKEditorField


class Update(url_tracker.URLTrackingMixin, models.Model):
    description = CKEditorField(blank=True)
    post_date = models.DateField(verbose_name='Date')

    class Meta:
        ordering = ["-post_date"]

    def clean(self):
        self.description = self.description.strip()

    def __str__(self):
        return str(self.post_date.isoformat())

    def get_absolute_url(self):
        return reverse('update-detail', kwargs={'pk': self.pk})

    def dependent_paths(self):
        yield reverse('update-list')


class UpdatePhoto(BasePhoto):
    content_object = models.ForeignKey(Update, related_name='photos')

url_tracker.track_url_changes_for_model(Update)
dumper.register(Update)
dumper.register(UpdatePhoto)
simpleimages.trackers.track_model(UpdatePhoto)
