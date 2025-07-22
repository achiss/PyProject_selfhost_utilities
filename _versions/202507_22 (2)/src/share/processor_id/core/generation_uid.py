from typing import overload
from typing import Tuple, Union
from uuid import UUID
from uuid import uuid4, uuid5


@overload
def generate() -> Tuple[bool, UUID]: ...


@overload
def generate(domain: UUID, object_data: str) -> Tuple[bool, UUID]: ...


def generate(domain: UUID = None, object_data: str = None) -> Tuple[bool, Union[UUID, str]]:
    if domain is None and object_data is None:
        try:
            return True, uuid4()
        except Exception as e:
            return False, str(e)
    elif domain and object_data:
        try:
            return True, uuid5(namespace=domain, name=object_data)
        except Exception as e:
            return False, str(e)
    return False, "Invalid arguments"


if __name__ == '__main__':
    print(generate())