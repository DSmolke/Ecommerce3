from dataclasses import dataclass
from decimal import Decimal

from ecommerce3.ecommerceapp.util.loader import EnumLoader, JsonReader
from ecommerce3.ecommerceapp.util.validator import EnumValidator

# IDEA Maybe I should initialise this enum in settings.py
Category = EnumLoader('Category', JsonReader(file_path=r"../files/categories.json"), EnumValidator).load()

@dataclass
class Client:
    """ Client object used to represent service customer"""
    name: str
    surname: str
    age: int
    preferences: list[int]


@dataclass
class Product:
    """ Product object used for orders """
    name: str
    quantity: int
    price: Decimal
    category: Category
