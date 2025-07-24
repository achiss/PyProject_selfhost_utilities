from typing import Tuple
from typing import overload
from uuid import UUID
from uuid import uuid4, uuid5


@overload
def generate_uid() -> Tuple[bool, UUID | str]: ...


@overload
def generate_uid(domain: UUID, object_string: bytes) -> Tuple[bool, UUID | str]: ...


def generate_uid(domain: UUID = None, object_string: bytes = None) -> Tuple[bool, UUID | str]:
	""" Base method: id generation """
	
	if not domain:
		try:
			return True, uuid4()
		
		except Exception as e:
			return False, f'UUID generation (version 4), unexpected error: {e}'

	else:
		try:
			return True, uuid5(domain, object_string)

		except Exception as e:
			return False, f'UUID generation (version 5), unexpected error: {e}'
