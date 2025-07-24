from typing import Tuple, Type, Any

from data.pattern import REGEX_UUID, REGEX_UUID4, REGEX_UUID5


class ValidatorID:
    @staticmethod
    def check_uuid(uuid_number: str, version_type: str | None) -> Tuple[bool, None | str, Type[Any] | None]:

        """
        Args:
            uuid_number (str): checked id number
            version_type (str or None): uuid version type - uuid, uuid4, uuid5 (Default: None)

        Returns:
            - True, None, None - if success
            - False, message (str), error type - if false
        """

        validate = {
            None: lambda x: REGEX_UUID4.fullmatch(uuid_number) or REGEX_UUID5.fullmatch(uuid_number),
            'UUID': lambda x: REGEX_UUID.fullmatch(uuid_number),
            'UUID4': lambda x: REGEX_UUID4.fullmatch(uuid_number),
            'UUID5': lambda x: REGEX_UUID5.fullmatch(uuid_number),
        }

        _verify_func = validate.get(version_type.upper() if version_type else None)
        if _verify_func(uuid_number):
            return True, None, None

        _message: str = {
            None: 'UUID4 (version 4) or UUID5 (version 5)',
            'UUID': 'UUID',
            'UUID4': 'UUID4 (version 4)',
            'UUID5': 'UUID5 (version 5)',
        }.get(version_type.upper() if version_type else None)
        _message: str = f'verify ID number error: does not match "{_message}" pattern(s)'
        return False, _message, ValueError
