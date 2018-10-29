from django.test import TestCase
from model_mommy import mommy

from .models import WebContent

SAMPLE_CONTENT = """
# Sample markdown

- A list
- With two itens
"""


class WebContentTestCase(TestCase):

    def test_web_content(self):
        content = mommy.make(
            WebContent,
            title="a title",
            markdown_content=SAMPLE_CONTENT)

        content.save()
        self.assertEqual(content.slug, "a-title")
