import pytest

from ecommerce3.ecommerceapp.util.loader import JsonReader
from ecommerce3.settings import FilenameException


class TestJsonReader:
    @pytest.mark.xfail(reason="If test will run outside od tests dir, error may occur.")
    def test_with_valid_file_path(self) -> None:
        assert JsonReader(file_path="./tests_files/test_correct_path.json").read() == []

    def test_with_invalid_file_path(self) -> None:
        """ Standard behaviour when file does not exist """
        with pytest.raises(FileNotFoundError) as e:
            JsonReader(file_path="incorrect.json").read()
        assert e.type == FileNotFoundError

    def test_with_invalid_file_type(self) -> None:
        """ Exception raised whenever filename is not referring to json """
        with pytest.raises(Exception) as e:
            JsonReader(file_path="../../tests_files/test_incorrect_type.txt").read()
        assert e.type == FilenameException
