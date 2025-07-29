from uuid import UUID
from typing import Any


def check_id_type(value: UUID | str) -> bool: return bool(isinstance(value, (UUID, str)))


def check_id_length(value: UUID | str) -> bool: return len(value) == 36


def check_length(value: Any, reference_length: int,
                 is_equal: bool = False, is_less: bool = False, is_greater: bool = False) -> bool:

    _length: int = len(value)

    if is_equal:
        return _length == reference_length

    elif is_less and is_equal:
        return _length <= reference_length

    elif is_less and not is_equal:
        return _length < reference_length

    elif is_greater and is_equal:
        return _length >= reference_length

    elif is_greater and not is_equal:
        return _length > reference_length

    else:
        raise AttributeError('Parameters "is_less" and "is_greater" cannot be True at the same time')

