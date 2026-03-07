from django.test import TestCase


class BasicTest(TestCase):

    def test_homepage(self):
        """Basic test to confirm test suite runs"""
        self.assertEqual(1, 1)
