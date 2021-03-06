from django.contrib.flatpages.models import FlatPage
from django.core.urlresolvers import reverse

import dumper


def flatpage_dependent_paths(self):
    yield reverse('exhibition-current')
    yield reverse('contact')

FlatPage.dependent_paths = flatpage_dependent_paths

dumper.register(FlatPage)
