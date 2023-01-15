from typing import Any


def is_int(value: Any) -> bool:
    """
    Function made, because I wanted to have ability to check in a class if some value is integer and not break Dependency Inversion Principle.
    That would happen if I would just use isinstance builtin function.
    """
    return isinstance(value, int)
