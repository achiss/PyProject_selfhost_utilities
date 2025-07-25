from typing import Type, Any, Tuple


def check_data_type(*data_type: Type[Any], checked_value: Any) -> Tuple[bool, str | None, Type[Exception] | None]:

	if len(data_type) == 0:
		_message: str = f'incorrect list of values data type - is empty, should be defined'
		return False, _message, ValueError
	
	if any(isinstance(checked_value, argument_data_type) for argument_data_type in data_type):
		return True, None, None
	
	else:
		expected_types: str = ', '.join(data_type.__name__ for data_type in data_type)
		received_type: str = str(type(checked_value).__name__)

		_message: str = f'invalid data type - expected {expected_types}, got {received_type}'
		return False, _message, TypeError
