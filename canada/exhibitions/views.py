from django.shortcuts import get_object_or_404, render
from django.conf import settings


from exhibitions.models import Exhibition


def single(request, year, name):
    exhibition = get_object_or_404(Exhibition, start_date__year=year, name=name)
    context = {
        'image_size': settings.CANADA_SLIDER_IMAGE_SIZE,
        'exhibition': exhibition
    }
    return render(request, 'exhibitions/single.html', context)
