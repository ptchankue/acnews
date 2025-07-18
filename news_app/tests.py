"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self) -> None:
        """
        Tests that 1 + 1 always equals 2.
        """
        assert 1 + 1 ==  2


__test__ = {
    "doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""
}

class BlogTest(TestCase):

    def setUp(self):
        pass

    def test_Get_blog(self):
        resp = self.client.get("/blog")

        print(resp.status_code)
        assert resp.status_code == 200
