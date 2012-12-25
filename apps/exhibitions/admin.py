from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from .models import Exhibition
from libs.common.admin import PhotoInline


class ExhibitionAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = [PhotoInline]
    date_hierarchy = 'start_date'
    list_display = ('name', 'start_date')
    fields = ('name', 'description', ('start_date', 'end_date'), 'artists',)

admin.site.register(Exhibition, ExhibitionAdmin)