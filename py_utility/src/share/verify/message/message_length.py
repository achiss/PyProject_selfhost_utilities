from typing import Any


def from_length_equal(checked_length: int | float,
                      reference_length: int | float) -> str:

    return f'incorrect object length: {checked_length} should be equal {reference_length}'


def from_length_less(checked_length: int | float,
                     reference_length: int | float,
                     as_equal: bool) -> str:

    if not as_equal:
        return f'incorrect object length: {checked_length} should be less than {reference_length}'

    return f'incorrect object length: {checked_length} should be less or equal than {reference_length}'


def from_length_greater(checked_length: int | float,
                        reference_length: int | float,
                        as_equal: bool) -> str:

    if not as_equal:
        return f'incorrect object length: {checked_length} should be greater than {reference_length}'

    return f'incorrect object length: {checked_length} should be greater or equal than {reference_length}'


def from_unexpected(description: Any) -> str:

    return f'unexpected error during verification length: {description}'
