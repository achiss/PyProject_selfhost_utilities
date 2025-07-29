from typing import Tuple, Type

from src.share.verify.pattern.regex_uuid import REGEX_UUID, REGEX_UUID4, REGEX_UUID5
from src.share.verify.message.message_value_uuid import from_data_type, from_uuid, from_unexpected


def verify_uuid(uuid_string: str) -> Tuple[bool, str | None, Type[Exception] | None]:

    try:
        if not isinstance(uuid_string, str):
            _message: str = from_data_type(
                checked_data_type = type(uuid_string),
                reference_data_type = str,
            )
            return False, _message, TypeError

        _result: bool = bool(REGEX_UUID.fullmatch(string = uuid_string))
        if not _result:
            _message: str = from_uuid(is_common = True)
            return False, _message, None

        return True, None, None

    except Exception as e:
        _message: str = from_unexpected(description = e)
        return False, _message, type(e)


def verify_uuid_v4_v5(uuid_string: str) -> Tuple[bool, str | None, Type[Exception] | None]:

    try:
        if not isinstance(uuid_string, str):
            _message: str = from_data_type(
                checked_data_type = type(uuid_string),
                reference_data_type = str,
            )
            return False, _message, TypeError

        _result: bool = bool(REGEX_UUID4.fullmatch(string = uuid_string) or REGEX_UUID5.fullmatch(string = uuid_string))
        if not _result:
            _message: str = from_uuid(is_common = False)
            return False, _message, None

        return True, None, None

    except Exception as e:
        _message: str = from_unexpected(description = e)
        return False, _message, type(e)


def check_uuid(uuid_string: str, is_common: bool) -> Tuple[bool, str | None, Type[Exception] | None]:

    if is_common:
        return verify_uuid(uuid_string)

    return verify_uuid_v4_v5(uuid_string)
