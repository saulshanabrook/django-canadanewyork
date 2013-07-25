from django.contrib import admin
from django.forms import Textarea, ModelForm
from django.utils.safestring import mark_safe
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm


class CKEditorWidget(Textarea):
    class Media:
        js = ('canada/ckeditor/ckeditor.js',)

    def render(self, name, value, attrs=None):
        output = super(CKEditorWidget, self).render(name, value, attrs)
        output += mark_safe(
            '<script type="text/javascript">CKEDITOR.replace("{}");</script>'
            .format(name)
        )
        return output


def editor_form(field_names):
    class EditorForm(ModelForm):
        class Meta:
            widgets = dict.fromkeys(field_names, CKEditorWidget())
    return EditorForm


class EditorFlatPageForm(FlatpageForm):
    class Meta(object):
        model = FlatPage
        widgets = {'content': CKEditorWidget()}


class EditorFlatPageAdmin(FlatPageAdmin):
    form = EditorFlatPageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, EditorFlatPageAdmin)