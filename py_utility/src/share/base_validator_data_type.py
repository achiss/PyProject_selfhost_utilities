from typing import Type, Any, Tuple


def check_data_type(*data_type: Type[Any], checked_value: Any) -> Tuple[bool, str | None, Type[Exception] | None]:
	
	from src.share import EMPTY_LIST_ERROR_TEMPLATE, TYPE_ERROR_TEMPLATE
	
	if len(data_type) == 0:
		return False, EMPTY_LIST_ERROR_TEMPLATE.format('data type'), ValueError
	
	if any(isinstance(checked_value, argument_data_type) for argument_data_type in data_type):
		return True, None, None
	
	else:
		expected_types: str = ', '.join(data_type.__name__ for data_type in data_type)
		received_type: str = str(type(checked_value).__name__)
		
		return False, TYPE_ERROR_TEMPLATE.format(expected_types, received_type), TypeError
