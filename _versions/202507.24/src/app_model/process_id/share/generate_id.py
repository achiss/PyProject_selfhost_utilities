from typing import overload
from typing import Tuple, Type, Any
from uuid import UUID
from uuid import uuid4, uuid5


@overload
def generate_id() -> Tuple[bool, str | UUID, None | Type[Any]]: ...


@overload
def generate_id(domain: UUID, object_string: str) -> Tuple[bool, str | UUID, None | Type[Any]]: ...


def generate_id(domain: UUID = None, object_string: str = None) ->  Tuple[bool, str | UUID, None | Type[Any]]:
    """ Base method: generation ID (UUID4 | UUID5) """

    if not (domain and object_string):
        try:
            _data: UUID = uuid4()
            return True, _data, None

        except Exception as e:
            _message: str = f'unexpected error: failed to generate ID number (version UUID4) - {e}'
            return False, _message, type(e)

    elif domain and object_string:
        try:
            _data: UUID = uuid5(namespace=domain, name=object_string)
            return True, _data, None

        except Exception as e:
            _message: str = f'unexpected error: failed to generate ID number (version UUID5) - {e}'
            return False, _message, type(e)

    else:
        _message: str = f'incorrect arguments function'
        return False, _message, ValueError


if __name__ == '__main__':
    print(generate_id())
