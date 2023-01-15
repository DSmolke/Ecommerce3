import unittest

from enum import Enum
from unittest import TestCase
from unittest.mock import patch

from ecommerce3.ecommerceapp.util.loader import JsonReader, EnumLoader
from ecommerce3.settings import FilenameException
# Import needed to mock EnumValidator object
from ecommerce3.ecommerceapp.util.validator import EnumValidator


class TestJsonReader(TestCase):
    # If test will run outside od tests dir, error may occur.
    @unittest.expectedFailure
    def test_with_valid_file_path(self) -> None:
        self.assertEquals(JsonReader(file_path="./tests_files/test_correct_path.json").read(), [])

    def test_with_invalid_file_path(self) -> None:
        """ Standard behaviour when file does not exist """
        with self.assertRaises(FileNotFoundError):
            JsonReader(file_path="incorrect.json").read()

    def test_with_invalid_file_type(self) -> None:
        """ Exception raised whenever filename is not referring to json """
        with self.assertRaises(FilenameException):
            JsonReader(file_path="../../tests_files/test_incorrect_type.txt").read()


class TestEnumLoader(TestCase):
    def test_with_valid_arguments(self):
        """
        Mocks:
            - JsonReaderMock of JsonReader
            - EnumValidatorMock of EnumValidator

        Test checks if new Enum instance is created
        """
        with patch('ecommerce3.tests.test_ecommerceapp.test_util.test_loader.JsonReader') as JsonReaderMock:
            JsonReaderMock.read.return_value = {"A": 1, "B": 2}
            with patch('ecommerce3.tests.test_ecommerceapp.test_util.test_loader.EnumValidator') as EnumValidatorMock:
                EnumValidatorMock.validate.return_value = None

                self.assertIsInstance(EnumLoader("Category", JsonReaderMock, EnumValidatorMock).load(),
                                      type(Enum("Category", {"A": 1, "B": 2})))

    # TODO add additional test for cases where reader, validator or name is not valid


if __name__ == "__main__":
    unittest.main()
