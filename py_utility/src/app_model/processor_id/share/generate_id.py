from uuid import UUID
from typing import overload
from typing import Tuple, Type

from src.app_model.processor_id.share.base_method.generate_id_versions import get_uuid4, get_uuid5


BASE_MESSAGE: str = 'method generate ID failed'


def verification_data(domain: UUID | None, object_data: str | None) -> Tuple[bool, str | None, Type[Exception] | None]:
	
	if domain and object_data:
		if not isinstance(domain, UUID):
			_message: str = f'{BASE_MESSAGE}: invalid "domain" type - expected "UUID" or "str", got "{type(domain)}"'
			return False, _message, TypeError
		
		if not isinstance(object_data, str):
			_message: str = f'{BASE_MESSAGE}: invalid "object data" type - expected "str", got "{type(object_data)}"'
			return False, _message, TypeError
		
		if len(object_data.strip()) == 0:
			_message: str = f'{BASE_MESSAGE}: invalid "object data" value - cannot be empty or whitespace'
			return False, _message, ValueError
	
	return True, None, None


def generate_uuid4() -> Tuple[bool, str | UUID, Type[Exception] | None]:

	try:
		_received_data: UUID = get_uuid4()
		return True, _received_data, None
	
	except (OSError, NotImplementedError) as e:
		_message: str = f'{BASE_MESSAGE}: system error during generation "UUID version 4" - {e}'
		return False, _message, type(e)
	
	except Exception as e:
		_message: str = f'{BASE_MESSAGE}: unexpected error during generation "UUID version 4" - {e}'
		return False, _message, type(e)


def generate_uuid5(domain: UUID, object_data: str) -> Tuple[bool, str | UUID, Type[Exception] | None]:
	try:
		_received_data: UUID = get_uuid5(domain, object_data)
		return True, _received_data, None
	
	except (OSError, NotImplementedError) as e:
		_message: str = f'{BASE_MESSAGE}: system error during generation "UUID version 5" - {e}'
		return False, _message, type(e)
	
	except Exception as e:
		_message: str = f'{BASE_MESSAGE}: unexpected error during generation "UUID version 5" - {e}'
		return False, _message, type(e)


@overload
def generate_id() -> Tuple[bool, str | UUID, Type[Exception] | None]: ...


@overload
def generate_id(domain: UUID, object_data: str) -> Tuple[bool, str | UUID, Type[Exception] | None]: ...


def generate_id(domain: UUID = None, object_data: str = None) -> Tuple[bool, str | UUID, Type[Exception] | None]:
	
	if not (_result := verification_data(domain, object_data))[0]:
		return False, _result[1], _result[2]

	if not (domain or object_data):
		return generate_uuid4()

	else:
		return generate_uuid5(domain, object_data)
