from typing import Optional


def print_name(name: str) -> None:
    print(name.capitalize())


def even_or_none(number: Optional[int]) -> Optional[int]:
    if number is None:
        return None
