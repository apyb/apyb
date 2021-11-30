import os

from django.contrib.staticfiles.finders import find
from django.templatetags.static import static
from django.http import Http404
from django.views.generic import TemplateView
from django_markup.markup import formatter

from .models import WebContent

HERO_ROOT = 'website/img/hero'
HERO_PHOTOS = sorted([
    static(f'{HERO_ROOT}/{img}') for img in os.listdir(find(HERO_ROOT))
], reverse=True)


class Home(TemplateView):

    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['hero_photos'] = HERO_PHOTOS

        return context


class Markdown(TemplateView):
    template_name = 'website/markdown.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            web_content = WebContent.objects.get(slug=kwargs['slug'])
        except WebContent.DoesNotExist:
            raise Http404("WebContent does not exist")

        context['markdown_content'] = formatter(
            web_content.markdown_content,
            filter_name='markdown',
            safe_mode=False)

        return context
