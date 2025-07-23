from typing import overload
from typing import Tuple, Type, Any
from uuid import UUID


@overload
def convert_id(uuid_value: UUID) -> Tuple[bool, str | UUID, None | Type[Any]]: ...


@overload
def convert_id(uuid_value: str) -> Tuple[bool, str | UUID, None | Type[Any]]: ...


def convert_id(uuid_value: UUID | str = None) -> Tuple[bool, str | UUID, None | Type[Any]]:
    """ Base method: converting ID """

    if isinstance(uuid_value, UUID):
        try:
            _data: str = str(uuid_value)
            return True, _data, None

        except Exception as e:
            return False, f'unexpected error: failed to converse "UUID" to "str" type - {e}', type(e)

    elif isinstance(uuid_value, str):
        try:
            _data: UUID = UUID(uuid_value)
            return True, _data, None

        except Exception as e:
            return False, f'unexpected error: failed to converse "str" to "UUID" type - {e}', type(e)

    else:
        return False, f'invalid data type: expected "str or UUID", got "{type(uuid_value).__name__}"', TypeError
