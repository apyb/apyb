import os

from django.contrib.staticfiles.finders import find
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.views.generic import TemplateView
from django_markup.markup import formatter

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

class About(TemplateView):
    template_name = 'website/markdown.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        markdown_content = open("website/markdown/about.md", 'r').read()
        context['markdown_content'] = formatter(markdown_content, filter_name='markdown', safe_mode=False)
        return context