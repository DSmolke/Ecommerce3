import json

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, ClassVar

from smolke_data.common.validator.string import matches_regex

from ecommerce3.ecommerceapp.util.validator import Validator
from ecommerce3.settings import Regex, FilenameException


class FileReader(ABC):
    """ Abstraction of file reader """
    @abstractmethod
    def read(self) -> Any:
        """"""
        pass


@dataclass
class JsonReader(FileReader):
    """
    File reader designed to load data form json files. Modular structure allows changing
    filename validation rules and filename validator itself.
    """
    file_path: str
    file_path_regex: ClassVar = Regex.JSON_FILENAME
    file_path_validator: Callable[[str, str], bool] = matches_regex

    def __post_init__(self):
        """ Validates if provided filepath is correct in terms of file type"""
        if not self.file_path_validator(self.file_path, self.file_path_regex):
            raise FilenameException

    def read(self) -> Any:
        """ Reads json file and returns it in same form how it was structured in source file"""
        with open(self.file_path, 'r') as f:
            return json.load(f)


class Loader(ABC):
    """ Abstraction of object loader """
    @abstractmethod
    def load(self) -> Any:
        pass


@dataclass(eq=False)
class EnumLoader(Loader):
    """
    EnumLoader takes arguments:
    - name of Enum that he will create,
    - reader which will provide dict that will store enum object names and values,
    - validator which will validate if dict provided by reader is correct for new enum purposes
    """
    name: str
    reader: FileReader
    validator: Validator.__class__

    def load(self) -> Any:
        """
        Uses name, reader, and validator from instance namespace to create new Enum instance
        :return: <'self.name' enum>
        """
        enum_data = self.reader.read()
        self.validator(enum_data).validate()
        return Enum(self.name, enum_data)
