from typing import Tuple, Type
from uuid import UUID


def convert_data(uuid_string: UUID | str) -> Tuple[bool, str | UUID, Type[Exception] | None]:
	
	from src.app_model.processor_id.share.base_method.convert_data_type import uuid_to_str, str_to_uuid

	_base_message: str = 'converting ID failed'
	
	try:
		_value_id: UUID | str = ''
		if isinstance(uuid_string, UUID):
			_value_id: str = uuid_to_str(uuid_string)
		
		else:
			_value_id: UUID = str_to_uuid(uuid_string)
		
		return True, _value_id, None
	
	except Exception as e:
		_message: str = f'{_base_message}: {UNEXPECTED_ERROR.format(e)}'
		return False, _message, type(e)
