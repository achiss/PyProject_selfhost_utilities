from uuid import UUID
from typing import Tuple
from typing import overload

from src.share import get_uuid4, get_uuid5


@overload
def generate_id() -> Tuple[bool, UUID | str]: ...


@overload
def generate_id(domain: UUID, object_string: str) -> Tuple[bool, UUID | str]: ...


def generate_id(domain: UUID = None, object_string: str = None) -> Tuple[bool, UUID | str]:
    """ Base method: generate UUID (version 4/5) """

    from src.share.processor_id.core.base_uuid_message import get_message_system_error, get_message_unexpected_error

    if not (domain or object_string):
        try:
            return True, get_uuid4()

        except (OSError, NotImplementedError) as e:
            return False, get_message_system_error(uuid_version=4, description=e)

        except Exception as e:
            return False, get_message_unexpected_error(uuid_version=4, description=e)

    else:
        try:
            return True, get_uuid5(domain, object_string)

        except (OSError, NotImplementedError) as e:
            return False, get_message_system_error(uuid_version=5, description=e)

        except Exception as e:
            return False, get_message_unexpected_error(uuid_version=5, description=e)
