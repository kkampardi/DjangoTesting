from django.test import TestCase

from .models import Entry

class EntryModelTest(TestCase):
    """Ensure that the a blog's entry string representation is qual to its title"""

    def test_string_representation(self):
        entry = Entry(title="This is a test title")
        self.assertEqual(str(entry), entry.title)