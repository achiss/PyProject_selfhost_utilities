from typing import Tuple, Type
from uuid import UUID

from src.app_model.processor_id.share.base_converting_method import uuid_to_str, str_to_uuid


BASE_MESSAGE: str = 'converting ID failed'


def is_valid(value: UUID | str) -> Tuple[bool, str | UUID, Type[Exception] | None] | None:

    from src.app_model.processor_id.share.base_validation_method import check_id_type, check_id_length

    if not check_id_type(value):
        _message: str = f'{BASE_MESSAGE}: invalid ID type - expected "UUID" or "str", got "{type(value)}"'
        return False, _message, TypeError

    if isinstance(value, str) and not check_id_length(value):
        _message: str = f'{BASE_MESSAGE}: incorrect ID length - expected "36", got "{len(value)}"'
        return False, _message, ValueError


def convert_id(uuid_string: UUID | str) -> Tuple[bool, str | UUID, Type[Exception] | None]:

    is_valid(uuid_string)

    try:
        _received_id: UUID | str = ''
        if isinstance(uuid_string, UUID):
            _received_id = uuid_to_str(uuid_string)

        else:
            _received_id = str_to_uuid(uuid_string)

        return True, _received_id, None

    except Exception as e:
        _message: str = f'{BASE_MESSAGE}: unexpected error - {e}'
        return False, _message, type(e)


if __name__ == '__main__':
    print(convert_id(uuid_string=UUID('550e8400-e29b-41d4-a716-446655440000')))
