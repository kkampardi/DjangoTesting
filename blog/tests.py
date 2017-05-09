from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Entry

class EntryModelTest(TestCase):
    """Ensure that the a blog's entry string representation is qual to its title"""

    def test_string_representation(self):
        entry = Entry(title="This is a test title")
        self.assertEqual(str(entry), entry.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")


class HomePageTest(TestCase):
    """Test whether our blog entries show up on the homepage"""
    def setUp(self):
        self.user = get_user_model().objects.create(username="some_user")

    def test_homepage(self):
        response = self.client.get('/blog/list')
        self.assertEqual(response.status_code, 200)

    def test_one_entry(self):
        Entry.objects.create(title='1-title', body='1-body', author=self.user)
        response = self.client.get('/blog/list')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')

    def test_no_entries(self):
        response = self.client.get('/blog')
        self.assertContains(response, 'No blog entries yet')

    def test_two_entries(self):
        Entry.objects.create(title='1-title', body='1-body', author=self.user)
        Entry.objects.create(title='2-title', body='2-body', author=self.user)
        response = self.client.get('/')
        self.assertContains(response, '1-title')
        self.assertContains(response, '1-body')
        self.assertContains(response, '2-title')