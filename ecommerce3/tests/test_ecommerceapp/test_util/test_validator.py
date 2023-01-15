import unittest
from unittest import TestCase

from ecommerce3.ecommerceapp.util.validator import EnumValidator


class TestEnumValidatorCreation(TestCase):
    """ Checks if TypeError ocurs when invalid 'data' type provided"""
    def test_with_invalid_data_argument(self):
        with self.assertRaises(TypeError):
            EnumValidator(data=1)


class TestEnumValidator:

    class TestValidate(TestCase):
        """ Checks if EnumValidator.validate method works correctly """
        def test_with_valid_data(self) -> None:
            valid_data = {"A": 1, "B": 2}
            self.assertIs(EnumValidator(valid_data).validate(), None)

        def test_with_invalid_data(self) -> None:
            for invalid_data in [{"a": 1}, {"A": "1"}]:
                with self.subTest(i=invalid_data):
                    with self.assertRaises(ValueError):
                        EnumValidator(invalid_data).validate()


if __name__ == "__main__":
    unittest.main()
