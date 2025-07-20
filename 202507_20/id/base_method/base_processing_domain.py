from uuid import UUID
from typing import Tuple


def base_processing_domain(value: UUID | str) -> Tuple[bool, str]:
	if isinstance(value, UUID):
		value: str = str(value)
		return True, value
	
	elif isinstance(value, str):
		return True, value
	
	else:
		return False, f'argument (domain) type error: {value}'
