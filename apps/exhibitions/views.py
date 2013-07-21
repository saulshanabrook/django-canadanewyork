from django.views.generic import DetailView
from django.contrib.flatpages.models import FlatPage

from .models import Exhibition
from libs.common.views import ObjectList, ObjectListFromParent


class ExhibitionList(ObjectList):
    queryset = Exhibition.objects.all()


class ExhibitionDetail(DetailView):
    queryset = Exhibition.objects.prefetch_related('photos')


class ExhibitionPressList(ObjectListFromParent):
    queryset = Exhibition.objects.only('name').prefetch_related('press')

    def get_object_list_from_parent(self, exhibition):
        return exhibition.press.all()


class ExhibitionCurrent(DetailView):
    template_name = 'exhibitions/exhibition_current.html'

    def get_object(self):
        return Exhibition.objects.get(current=True)

    def get_context_data(self, **kwargs):
        context = super(ExhibitionCurrent, self).get_context_data(**kwargs)
        flatpage = FlatPage.objects.filter(url__exact='/')
        content = flatpage.values_list('content', flat=True)
        if content:
            context['extra_content'] = content[0]
        return context
