from typing import Tuple, Type
from uuid import UUID


def verification_convert_data(uuid_string: UUID | str) -> Tuple[bool, str | None, Type[Exception] | None]:
	
	from src.app_model.processor_id.share.base_method.validate_data import check_id_type, check_id_length, check_uuid
	from src.app_model.processor_id.share.message.module_message import DATA_TYPE_ERROR, LENGTH_ERROR, FMT_ERROR_COMMON
	
	_base_message: str = 'verification convert data failed'
	
	if not check_id_type(uuid_string):
		_message: str = f'{_base_message}: {DATA_TYPE_ERROR.format(type(uuid_string))}'
		return False, _message, TypeError
	
	if isinstance(uuid_string, str):
		if not check_id_length(uuid_string):
			_message: str = f'{_base_message}: {LENGTH_ERROR.format(len(uuid_string))}'
			return False, _message, ValueError
		
		if not check_uuid(uuid_string):
			_message: str = f'{_base_message}: {FMT_ERROR_COMMON.format(uuid_string)}'
			return False, _message, ValueError
	
	return True, None, None
