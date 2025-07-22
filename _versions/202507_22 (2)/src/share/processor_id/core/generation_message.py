from typing import Any


def get_message_unsupported_error() -> str: return 'unsupported arguments'


def get_message_system_error(uuid_version: int, description: Any) -> str:
    return f'"id" generation (version {uuid_version}) system error: {description}'


def get_message_unexpected_error(uuid_version: int, description: Any) -> str:
    return f'"id" generation (version {uuid_version}) unexpected error: {description}'
