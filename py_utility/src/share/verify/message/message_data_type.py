from typing import Any


def from_data_type(checked_data_type: Any,
                   reference_data_type: Any) -> str:

    return f'invalid data type: expected "{checked_data_type}", got "{reference_data_type}"'


def from_length(checked_length: int | float,
                      reference_length: int | float) -> str:

    return f'incorrect object length: {checked_length} should be equal {reference_length}'


def from_unexpected(description: str | None) -> str:

    if isinstance(description, str):
        return f'unexpected error during verification method - {description}'

    return 'unexpected error during verification method'
