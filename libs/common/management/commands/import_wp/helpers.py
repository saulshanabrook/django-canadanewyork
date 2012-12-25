import os
import urlparse

import markdown2
import html2text
import requests
import requests_cache
import dateutil.parser
from bs4 import BeautifulSoup

from django.core.files.temp import NamedTemporaryFile
from django.core.files import File


requests_cache.configure(cache_name='static/wordpress/image_cache')


def html_to_markdown(html):
    html = html.replace('[gallery]', '')

    html = markdown2.markdown(html)
    html = html.replace('\n', '<br>')
    h = html2text.HTML2Text()
    h.ignore_images = True
    h.ignore_links = True
    h.body_width = 0
    h.unicode_snob = True

    html = h.handle(html)
    return html


def image_links_from_html(html):
    html = html.replace('[gallery]', '')
    soup = BeautifulSoup(html)
    for link in soup.find_all('a'):
        yield link.get('href')


def file_from_link(url):
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(requests.get(url).content)
    img_temp.flush()
    return os.path.basename(url), File(img_temp)


def year_from_element(element):
    full_url = element.findtext('link')
    url = urlparse.urlparse(full_url)
    path = url.path.split('/')[1:]
    return path[1]


def date_from_text(text, default):
    '''
    given a string will try to parse a date from that string
    '''
    try:
        date = dateutil.parser.parse(text, default=default, fuzzy=True)
    except ValueError:
        return None
    else:
        return date


def dates_from_text(text, year):
    '''
    Given a text string such as 'Show is during January 20th - February 1 2012'
    , will try to return the two dates. If only one date found, it will return
    that date and then None.

    A string of the year is required in case one isn't found
    '''
    default = dateutil.parser.parse(year)

    if len(text.split('-')) > 2:
        dates = (
            date_from_text(text.split('-')[-2], default),
            date_from_text(text.split('-')[-1], default),
        )
        if not all(dates):
            return dates[0] or dates[1] or default
        return (
            min(dates) or default,
            max(dates),
        )
    return date_from_text(text, default) or default, None


def models_from_text(text, model, model_function):
    '''
    Given a model, tries to find that model in the text, using the
    model_function of the model to search the text.
    '''
    for model_instance in model.objects.all():
        if model_function(model_instance).lower() in text.lower():
            yield model_instance