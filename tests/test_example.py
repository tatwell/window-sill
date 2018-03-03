"""

Example Test File

To run:

    nosetests -c nose.cfg
    python

"""
from unittest import TestCase
from unittest import skip


class AppTest(TestCase):

    def test_assert(self):
        self.assertTrue(True)

    @skip
    def test_skip(self):
        raise Exception("I should not be called.")
