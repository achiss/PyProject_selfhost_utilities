from typing import Any


def from_data_type(checked_data_type: Any,
                   reference_data_type: Any) -> str:

    return f'invalid data type: expected "{checked_data_type}", got "{reference_data_type}"'


def from_uuid(is_common: bool) -> str:

    if not is_common:
        return 'incorrect uuid (version 4 or version 5) string format'

    return 'incorrect uuid string format'


def from_unexpected(description: Any) -> str:

    return f'unexpected error during uuid verification: {description}'