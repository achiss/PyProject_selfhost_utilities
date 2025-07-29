from typing import Tuple, Type

from src.share.verify.message.message_range import from_parameters, from_range, from_unexpected


def verify_lower_value(checked_value: int | float,
                       lower_limit: int | float,
                       is_lower_body_include: bool) -> bool:

    return checked_value > lower_limit or (is_lower_body_include and checked_value == lower_limit)


def verify_upper_value(checked_value: int | float,
                       upper_limit: int | float,
                       is_upper_limit_include: bool) -> bool:

    return checked_value < upper_limit or (is_upper_limit_include and checked_value == upper_limit)


def check_range(checked_value: int | float,
                lower_limit: int | float,
                upper_limit: int | float,
                is_lower_limit_include: bool = False,
                is_upper_limit_include: bool = False) -> Tuple[bool, str | None, Type[Exception] | None]:

    try:
        if lower_limit > upper_limit:
            _message: str = from_parameters(
                lower_limit = lower_limit,
                upper_limit = upper_limit,
            )
            return False, _message, AttributeError

        if not (verify_lower_value(checked_value, lower_limit, is_lower_limit_include)
                or verify_upper_value(checked_value, upper_limit, is_upper_limit_include)):
            _message: str = from_range(
                checked_value = checked_value,
                lower_limit = lower_limit,
                upper_limit = upper_limit,
            )
            return False, _message, None

        return True, None, None

    except Exception as e:
        _message: str = from_unexpected(
            description = e,
        )
        return False, _message, type(e)
