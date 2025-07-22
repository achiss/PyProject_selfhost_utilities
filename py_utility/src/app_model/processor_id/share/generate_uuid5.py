from typing import Tuple
from uuid import UUID
from uuid import uuid5


def generate_uuid5(domain: UUID, object_string: str) -> Tuple[bool, UUID | str, None | str]:
	try:
		_uid = uuid5(namespace=domain, name=object_string)
		return True, _uid, None
	
	except (OSError, NotImplementedError) as e:
		_type: str = type(e).__name__
		_message: str = f''
		return False, _message, _type
	
	except Exception as e:
		_type: str = type(e).__name__
		_message: str = ''
		return False, _message, _type
