from typing import Tuple, Type
from uuid import UUID

from src.app_model.processor_id.share.base_conversion_method import uuid_to_str, str_to_uuid

BASE_MESSAGE: str = 'method convert ID failed'


def verification_uuid(value: UUID | str) -> Tuple[bool, str | None, Type[Exception] | None]:

    from src.app_model.processor_id.share.base_validation_method import check_id_type, check_id_length , check_id

    if not check_id_type(value):
        _message: str = f'{BASE_MESSAGE}: invalid ID type - expected "UUID" or "str", got "{type(value)}"'
        return False, _message, TypeError

    if isinstance(value, str):
        if not check_id_length(value):
            _message: str = f'{BASE_MESSAGE}: incorrect ID length - expected "36", got "{len(value)}"'
            return False, _message, ValueError
        
        if not check_id(value):
            _message: str = f'{BASE_MESSAGE}: incorrect ID format'
            return False, _message, ValueError
    
    return True, None, None


def convert_id(uuid_string: UUID | str) -> Tuple[bool, str | UUID, Type[Exception] | None]:

    if not (_result := verification_uuid(uuid_string))[0]:
        return False, _result[1], _result[2]

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
    pass
