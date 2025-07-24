from typing import Tuple, Type
from typing import overload


def verify_is_equal(checked_length: int, reference_length: int) -> Tuple[bool, str | None, Type[Exception] | None]:

	return (True, None, None) if (checked_length == reference_length) else (False, None, None)


def verify_is_less(checked_length: int, reference_length: int, is_equal: bool) \
	-> Tuple[bool, str | None, Type[Exception] | None]:

	return (True, None, None) \
		if ((checked_length < reference_length) or (is_equal and checked_length == reference_length)) else \
		(False, None, None)


def verify_as_greater(checked_length: int, reference_length: int, is_equal: bool) \
		-> Tuple[bool, str | None, Type[Exception] | None]:
	
	return (True, None, None) \
		if ((checked_length > reference_length) or (is_equal and checked_length == reference_length)) else \
		(False, None, None)


@overload
def check_length(checked_length: int, reference_length: int, is_equal: bool = True) \
		-> Tuple[bool, str | None, Type[Exception] | None]: ...


@overload
def check_length(checked_length: int, reference_length: int, is_less: bool, is_equal: bool = False) \
		-> Tuple[bool, str | None, Type[Exception] | None]: ...


@overload
def check_length(checked_length: int, reference_length: int, is_greater: bool, is_equal: bool = False) \
		-> Tuple[bool, str | None, Type[Exception] | None]: ...


def check_length(checked_length: int, reference_length: int,
                 is_less: bool = None, is_greater: bool = None, is_equal: bool = False) \
		-> Tuple[bool, str | None, Type[Exception] | None]:
	
	from src.share import ATTRIBUTE_ERROR_TEMPLATE
	
	if is_less and is_greater:
		_message: str = f'{ATTRIBUTE_ERROR_TEMPLATE} - "is_less" and "is_greater" cannot be True at the same time'
		return False, _message, AttributeError
		
	if is_greater:
		return verify_as_greater(checked_length, reference_length, is_equal)
		
	elif is_less:
		return verify_is_less(checked_length, reference_length, is_equal)
		
	elif is_equal:
		return verify_is_equal(checked_length, reference_length)
	
	else:
		_message: str = 'unhandled comparison case'
		return False, _message, RuntimeError
