from typing import Tuple, Type


def check_range(checked_value: int | float,
				minimal_value_bound: int | float,
				maximal_value_bound: int | float,
				is_lower_bound_included: bool,
				is_upper_bound_included: bool) -> Tuple[bool, str | None, Type[Exception] | None]:

	try:
		if minimal_value_bound > maximal_value_bound:
			_message: str = f'minimal value bound should be less or equal to maximal value bound'
			return False, _message, AttributeError

		if ((minimal_value_bound < checked_value < maximal_value_bound) or
				(is_lower_bound_included and minimal_value_bound == checked_value) or
				(is_upper_bound_included and maximal_value_bound == checked_value)):
			return True, None, None

		return False, None, None

	except Exception as e:
		_message: str = f'unexpected error during checking range - {e}'
		return False, _message, type(e)
