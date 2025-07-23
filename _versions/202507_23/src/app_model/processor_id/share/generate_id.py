from typing import overload
from typing import Tuple
from uuid import UUID

from src import generate_uuid4
from src.app_model.processor_id.share.generate_uuid5 import generate_uuid5


@overload
def generate_id() -> Tuple[bool, UUID | str, None | str]: ...


@overload
def generate_id(domain: UUID,
                object_name: str) -> Tuple[bool, UUID | str, None | str]: ...


def generate_id(domain: UUID = None,
                object_name: str = None) -> Tuple[bool, UUID | str, None | str]:
	
	""" Method: generate ID """
	
	if not (domain and object_name):
		return generate_uuid4()
	
	else:
		return generate_uuid5(domain, object_name)
