from typing import Tuple
from uuid import UUID
from uuid import uuid4


def generate_uuid4() -> Tuple[bool, UUID | str, None | str]:
	try:
		_uid = uuid4()
		return True, _uid, None
	
	except (OSError, NotImplementedError) as e:
		_type: str = type(e).__name__
		_message: str = f''
		return False, _message, _type
	
	except Exception as e:
		_type: str = type(e).__name__
		_message: str = ''
		return False, _message, _type
