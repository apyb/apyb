from django.test import TestCase
from model_bakery import baker

from .models import WebContent

SAMPLE_CONTENT = """
# Sample markdown

- A list
- With two itens
"""


class WebContentTestCase(TestCase):

    def test_web_content(self):
        content = baker.make(
            WebContent,
            title="a title",
            markdown_content=SAMPLE_CONTENT)

        content.save()
        self.assertEqual(content.slug, "a-title")
