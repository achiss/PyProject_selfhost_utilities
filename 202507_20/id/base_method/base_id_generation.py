from uuid import UUID
from uuid import uuid4, uuid5
from typing import Tuple
from typing import overload


@overload
def base_id_generation() -> Tuple[bool, UUID | str]: ...


@overload
def base_id_generation(domain: UUID, name_string: str) -> Tuple[bool, UUID | str]: ...


def base_id_generation(domain: UUID = None, name_string: str = None) -> Tuple[bool, UUID | str]:
	
	try:
		if not (domain and name_string):
			return True, uuid4()
			
		elif domain and name_string:
			return True, uuid5(domain, name_string)
			
		else:
			return False, f'invalid arguments values for ID generation (version: 4 or 5)'
	
	except (OSError, NotImplementedError) as e:
		return False, f'ID generation failed: {e}'
	
	except Exception as e:
		return False, f'ID generation unexpected error: {e}'
