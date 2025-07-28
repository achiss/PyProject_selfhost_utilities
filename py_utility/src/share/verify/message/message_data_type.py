from typing import Any


def from_data_type(checked_data_type: Any,
                   reference_data_type: Any) -> str:

    return f'invalid data type: expected "{checked_data_type}", got "{reference_data_type}"'
