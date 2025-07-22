from uuid import UUID
from typing import Tuple
from typing import overload

from src.share import check_uuid4, check_uuid5


@overload
def validate_id(uuid_number: str) -> Tuple[bool, None | str]: ...


@overload
def validate_id(uuid_number: UUID) -> Tuple[bool, None | str]: ...


def validate_id(uuid_number: str | UUID = None) -> Tuple[bool, None | str]:
    """ Base method: verification UUID (version 4/5) """

    from src.share.processor_id.core.base_uuid_message import get_message_unexpected_error

    if isinstance(uuid_number, UUID):
        try:
            uuid_number: str = str(uuid_number)

        except Exception:
            return False, get_message_unexpected_error(description='failed to convert from UUID to string')
    
    else:
        try:
            if not (check_uuid4(uuid_number) or check_uuid5(uuid_number)):
                return False, None

            return True, None

        except Exception as e:
            return False, get_message_unexpected_error(description=e)
