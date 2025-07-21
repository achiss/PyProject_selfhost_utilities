from typing import Tuple
from typing import overload
from uuid import UUID
from uuid import uuid4, uuid5


@overload
def generate_id() -> Tuple[bool, UUID | str]: ...


@overload
def generate_id(domain: UUID, object_string: str) -> Tuple[bool, UUID | str]: ...


def generate_id(domain: UUID = None, object_string: str = None) -> Tuple[bool, UUID | str]:

    try:
        if not domain:
            return True, uuid4()

        else:
            return True, uuid5(namespace=domain, name=object_string)

    except Exception as e:
        return False, f'ID generation unexpected error: {e}'
