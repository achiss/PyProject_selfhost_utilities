from typing import overload
from typing import Tuple
from uuid import UUID


@overload
def convert_id(uuid_number: str) -> Tuple[bool, UUID | str]: ...


@overload
def convert_id(uuid_number: UUID) -> Tuple[bool, UUID | str]: ...


def convert_id(uuid_number: str | UUID = None) -> Tuple[bool, UUID | str]:

    from src.share.processor_id.core.base_uuid_message import get_message_unexpected_error

    if isinstance(uuid_number, UUID):
        try:
            return True, str(uuid_number)

        except Exception:
            return False, get_message_unexpected_error(description='failed to convert from UUID to string')

    else:
        try:
            return True, UUID(uuid_number)

        except Exception:
            return False, get_message_unexpected_error(description='failed to convert from string to UUID')
