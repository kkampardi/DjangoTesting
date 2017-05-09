from django.test import TestCase

from .models import Entry

class EntryModelTest(TestCase):
    """Ensure that the a blog's entry string representation is qual to its title"""

    def test_string_representation(self):
        entry = Entry(title="This is a test title")
        self.assertEqual(str(entry), entry.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")


class ProjectTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/blog')
        self.assertEqual(response.status_code, 200)