import os

from django.contrib.staticfiles.finders import find
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.views.generic import TemplateView

HERO_ROOT = 'website/img/hero'
HERO_PHOTOS = sorted([
    static(f'{HERO_ROOT}/{img}') for img in os.listdir(find(HERO_ROOT))
], reverse=True)


class Home(TemplateView):

    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        context['hero_photos'] = HERO_PHOTOS

        return context
