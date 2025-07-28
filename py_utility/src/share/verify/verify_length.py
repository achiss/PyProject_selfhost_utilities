from typing import Tuple, Type

from src.share.verify.message.message_length import (from_length_equal, from_length_less, from_length_greater,
                                                     from_unexpected)


def check_equal(checked_value: int | float,
                reference_value: int | float) -> Tuple[bool, str | None, Type[Exception] | None]:

    try:
        if checked_value != reference_value:
            _message: str = from_length_equal(
                checked_length = checked_value,
                reference_length = reference_value,
            )
            return False, _message, None

        return True, None, None

    except Exception as e:
        _message: str = from_unexpected(
            description = str(e),
        )
        return False, _message, type(e)


def check_less(checked_value: int | float,
               reference_value: int | float,
               is_equal: bool = False) -> Tuple[bool, str | None, Type[Exception] | None]:

    try:
        if (checked_value > reference_value) or (is_equal and checked_value != reference_value):
            _message: str = from_length_less(
                checked_length = checked_value,
                reference_length = reference_value,
                as_equal = is_equal,
            )
            return False, _message, None

        return True, None, None

    except Exception as e:
        _message: str = from_unexpected(
            description = str(e),
        )
        return False, _message, type(e)


def check_greater(checked_value: int | float,
                  reference_value: int | float,
                  is_equal: bool = False) -> Tuple[bool, str | None, Type[Exception] | None]:

    try:
        if (checked_value < reference_value) or (is_equal and checked_value != reference_value):
            _message: str = from_length_greater(
                checked_length = checked_value,
                reference_length = reference_value,
                as_equal = is_equal,
            )
            return False, _message, None

        return True, None, None

    except Exception as e:
        _message: str = from_unexpected(
            description = str(e),
        )
        return False, _message, type(e)
