from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


@dataclass
class Client:
    name: str
    surname: str
    age: int
    preferences: list[int]


@dataclass
class Product:
    name: str
    quantity: int
    price: Decimal
    category: Category
