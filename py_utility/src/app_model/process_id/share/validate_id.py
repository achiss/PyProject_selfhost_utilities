from typing import Tuple, Type, Any

from src.validator import ValidatorID


def validate_id(uuid_number: str, version_type: str | None) -> Tuple[bool, None | str, Type[Any] | None]:
    """ Base method: verify ID """

    try:
        _flag, _result, _type = ValidatorID.check_uuid(uuid_number, version_type)
        if not _flag:
            return False, _result, _type

        return True, None, None

    except Exception as e:
        _message: str = f'unexpected error: failed to validate ID number "{uuid_number}" - {e}'
        return False, _message, type(e)
