from typing import Tuple, Type, Any, List
from uuid import UUID


def verify_object_data(*value: str) -> Tuple[bool, str | None, Type[Exception] | None]:
	
	if len(value) == 0:
		_message: str = f''
		return False, _message, ValueError
	
	elif len(value) == 1:
		_value: Any = value[0]
		if not isinstance(value[0], str):
			_message: str = f''
			return False, _message, TypeError
		
		_value: str = _value.strip()
		if len(_value) == 0:
			_message: str = f''
			return False, _message, ValueError
	
	else:
		errors_list: List[str] = []
		errors_type: List[Type[Exception]] = []
		for count, arg in enumerate(value):
			if not isinstance(arg, str):
				_message: str = f''
				errors_list.append(f'{count}: expected type {type(arg)}')
				errors_type.append(TypeError)
			
			arg = arg.strip()
			if len(arg) == 0:
				_message: str = f''
				errors_list.append(f'{count}: expected empty string')
				errors_type.append(ValueError)
		
		if len(errors_list) > 0:
			_message: str = f''
			return False, _message, TypeError


def verify_domain(value: UUID) -> Tuple[bool, str | None, Type[Exception] | None]:
	
	from src.app_model.processor_id.share.base_method.validate_data import check_id_type
	
	if not check_id_type(value):
		_message: str = f''
		return False, _message, TypeError
	
	return True, None, None


def verification_generate_data(*object_data: str, domain: UUID) -> Tuple[bool, str | None, Type[Exception] | None]:
	pass
