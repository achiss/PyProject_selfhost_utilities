from typing import Any


def from_parameters(lower_limit: int | float, upper_limit: int | float) -> str:

    return f'incorrect attributes, lower limit "{lower_limit} is greater then upper limit "{upper_limit}"'


def from_range(checked_value: int | float,
               lower_limit: int | float,
               upper_limit: int | float) -> str:

    return f'incorrect checked value, expected value "{checked_value}" not in the range "{lower_limit} - {upper_limit}"'


def from_unexpected(description: Any) -> str:

    return f'unexpected error during verification range: {description}'