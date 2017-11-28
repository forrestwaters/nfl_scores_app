from django.test import TestCase
from django.urls import resolve
from live_scores.views import scores

class SmokeTest(TestCase):

    def test_home_page_resolves_at_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, scores)
