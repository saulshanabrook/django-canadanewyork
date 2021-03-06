from django.db import models

import dumper

from libs.ckeditor.fields import CKEditorField


class CustomPage(models.Model):
    path = models.CharField(max_length=100, db_index=True)
    content = CKEditorField(blank=True)

    class Meta:
        verbose_name = 'custom page'
        verbose_name_plural = 'custom pages'
        ordering = ('path',)

    def __str__(self):
        return self.path

    def dependent_paths(self):
        yield self.path

dumper.register(CustomPage)
