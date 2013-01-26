import new

from django.db.models.fields import SlugField
from django.template.defaultfilters import slugify
from django.core.exceptions import FieldError

from south.modelsinspector import introspector


SLUG_INDEX_SEPARATOR = '-'    # the "-" in "foo-2"
# So that if used in filesystem, will not exceed max file length
MAX_LENGTH = 255 - len('.jpg')


class SlugifyField(SlugField):
    def __init__(self, *args, **kwargs):
        kwargs['editable'] = False

        kwargs['max_length'] = kwargs.get('max_length', MAX_LENGTH)
        # autopopulated slug is not editable unless told so
        self.populate_from = kwargs.pop('populate_from')
        # Use default seperator unless given one
        self.index_sep = kwargs.pop('sep', SLUG_INDEX_SEPARATOR)
        super(SlugifyField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        slug = self._get_value(model_instance)
        setattr(model_instance, self.attname, slug)
        return slug

    def _get_value(self, model_instance):
        if isinstance(self.populate_from, basestring):
            raise FieldError(
                ('In model {}, field {}, the populate_from kwarg needs to '
                 'be passed a list, not a string').format(model_instance,
                                                          self.attname))
        values = [value(model_instance) if callable(value) else getattr(model_instance, value) for value in self.populate_from]
        values = filter(None, values)
        return self.index_sep.join(map(slugify, values))[:MAX_LENGTH]

    def contribute_to_class(self, cls, name):
        super(SlugifyField, self).contribute_to_class(cls, name)
        setattr(
            cls,
            '_get_{}_value'.format(self.name),
            new.instancemethod(
                self._get_value,
                None,
                cls
            )
        )

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        args, kwargs = introspector(self)
        field_class = self.__class__.__module__ + "." + self.__class__.__name__
        kwargs.update({
            'populate_from': 'None' if any(map(callable, self.populate_from)) else repr(self.populate_from)
        })
        return (field_class, args, kwargs)
