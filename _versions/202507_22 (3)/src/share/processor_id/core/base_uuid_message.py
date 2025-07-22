from typing import overload
from typing import Any


def get_message_system_error(uuid_version: int, description: Any) -> str:
    return f'"id" generation (version {uuid_version}) system error: {description}'


@overload
def get_message_unexpected_error(uuid_version: int, description: Any) -> str: ...


@overload
def get_message_unexpected_error(description: Any) -> str: ...


def get_message_unexpected_error(uuid_version: int = None, description: Any = None) -> str:
    if uuid_version:
        return f'"id" generation (version {uuid_version}) unexpected error: {description}'

    else:
        return f'"id" generation unexpected error: {description}'

