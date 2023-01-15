from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable

from smolke_data.common.validator.string import matches_regex

from ecommerce3.validator.integer import is_int

class Validator(ABC):
    """ Validator abstraction """
    @abstractmethod
    def validate(self) -> None:
        pass

@dataclass
class EnumValidator(Validator):
    """ EnumValidator takes data, and value_validator as an arguments.(value_validator is set to is_int as a default """
    data: dict
    value_validator: Callable[[int], bool] = is_int

    def __post_init__(self):
        """ Initial validation to check if provided data argument is dict """
        if not isinstance(self.data, dict):
            raise TypeError("data argument is not dict")

    def validate(self) -> None:
        """
        Validates if dict is structured correctly, if not raises Exceptions.
        :return: None
        """
        if len([k for k in self.data.keys() if not matches_regex(k, r'^[A-Z]+(_?[A-Z]+)*$')]) != 0:
            raise ValueError('One of enum objects name is not valid')
        if len([v for v in self.data.values() if not self.value_validator(v)]) != 0:
            raise ValueError('One of enum objects value is not valid')
