from typing import Tuple, Type

from src.share.verify.message.message_range import from_unexpected


def check_range(checked_value: int | float,
                lower_value: int | float,
                upper_value: int | float,
                is_lower_include: bool = False,
                is_upper_include: bool = False) -> Tuple[bool, str | None, Type[Exception] | None]:

    try:
        pass

    except Exception as e:
        _message: str = from_unexpected(
            description = e,
        )
        return False, _message, type(e)
