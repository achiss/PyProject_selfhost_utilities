from typing import Tuple
from typing import overload
from uuid import UUID
from uuid import uuid4, uuid5


@overload
def generate_id() -> Tuple[bool, UUID | str]: ...


@overload
def generate_id(domain: UUID, object_string: bytes) -> Tuple[bool, UUID | str]: ...


def generate_id(domain: UUID = None, object_string: bytes = None) -> Tuple[bool, UUID | str]:
	""" Base method: generate_id """
	
	if not domain:
		try:
			return True, uuid4()
		
		except Exception as e:
			return False, f'id generation error (version 4): {e}'
	
	try:
		return True, uuid5(domain, object_string)
	
	except Exception as e:
		return False, f'id generation error (version 5): {e}'
