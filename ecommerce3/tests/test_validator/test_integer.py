import unittest
from unittest import TestCase
from ecommerce3.validator.integer import is_int


class TestIsInt(TestCase):
    def test_when_int(self):
        self.assertTrue(is_int(1))

    def test_when_not_int(self):
        self.assertFalse(is_int("1"))


if __name__ == "__main__":
    unittest.main()
