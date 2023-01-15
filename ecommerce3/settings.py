from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=False)
class Regex:
    JSON_FILENAME: ClassVar = r".*.json$"


# EXCEPTIONS
class FilenameException(Exception):
    pass

