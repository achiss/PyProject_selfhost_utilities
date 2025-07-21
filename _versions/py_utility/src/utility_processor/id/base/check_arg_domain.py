from typing import Tuple
from uuid import UUID


def check_arg_domain(value: UUID | str) -> Tuple[bool, UUID | str]:
	
	if isinstance(value, UUID):
		return True, value
	
	elif isinstance(value, str):
		value: UUID = UUID(value)
		return True, value
	
	else:
		return False, f'parameter (domain) incorrect data type: {type(value).__name__}'
