from uuid import UUID
from typing import Tuple, Type

from src.app_model.processor_id.share.base_method.validate_data import check_id_length, check_id, check_id_v4, check_id_v5


BASE_MESSAGE: str = 'method validate ID failed'


def validate_id(value: UUID | str, is_all_types: bool = False) -> Tuple[bool, str | None, Type[Exception] | None]:
	
	try:
		if isinstance(value, UUID):
			value: str = str(value)
		
		if not isinstance(value, str):
			_message: str = f'{BASE_MESSAGE}: invalid ID type - expected "UUID" or "str", got "{type(value)}"'
			return False, _message, TypeError
		
		if not check_id_length(value):
			_message: str = f'{BASE_MESSAGE}: incorrect ID length - expected "36", got "{len(value)}'
			return False, _message, ValueError
		
		if is_all_types and not check_id(value):
			_message: str = f'{BASE_MESSAGE}: incorrect ID format'
			return False, _message, ValueError
		
		if not is_all_types and not (check_id_v4(value) or check_id_v5(value)):
			_message: str = f'{BASE_MESSAGE}: incorrect ID formats (UUID versions 4 and 5)'
			return False, _message, ValueError
		
		return True, None, None
	
	except Exception as e:
		_message: str = f'{BASE_MESSAGE}: unexpected error - {e}'
		return False, _message, type(e)
