from typing import Tuple, Type
from typing import overload


def check_length_equal(checked_value: int | float, reference_value: int | float) -> bool:

	return checked_value == reference_value


def check_length_less(checked_value: int | float, reference_value: int | float, is_equal: bool) -> bool:

	if is_equal:
		return checked_value <= reference_value

	return checked_value < reference_value


def check_length_greater(checked_value: int | float, reference_value: int | float, is_equal: bool) -> bool:

	if is_equal:
		return checked_value >= reference_value

	return checked_value > reference_value


@overload
def check_length(checked_value: int | float, reference_value: int | float, is_equal: bool = True) \
	-> Tuple[bool, str | None, Type[Exception] | None]: ...


@overload
def check_length(checked_value: int | float, reference_value: int | float, is_less: bool, is_equal = False) \
	-> Tuple[bool, str | None, Type[Exception] | None]: ...


@overload
def check_length(checked_value: int | float, reference_value: int | float, is_greater: bool, is_equal = False) \
	-> Tuple[bool, str | None, Type[Exception] | None]: ...


def check_length(checked_value: int | float, reference_value: int | float,
				 is_less: bool = False, is_greater: bool = False, is_equal: bool = False) \
	-> Tuple[bool, str | None, Type[Exception] | None]:

	if is_less and is_greater:
		_message: str = f'arguments "is_less" and "is_greater" cannot be True at the same time'
		return False, _message, ValueError

	if is_less:
		_flag: bool = check_length_less(checked_value, reference_value, is_equal)
		return _flag, None, None

	elif is_greater:
		_flag: bool = check_length_greater(checked_value, reference_value, is_equal)
		return _flag, None, None

	else:
		_flag: bool = check_length_equal(checked_value, reference_value)
		return _flag, None, None
