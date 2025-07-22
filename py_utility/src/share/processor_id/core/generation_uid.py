from functools import singledispatch
from typing import Tuple, Any
from uuid import UUID
from uuid import uuid4, uuid5

from src.share.processor_id.interface import IGenerationUid


class GenerationUid(IGenerationUid):
    @classmethod
    @singledispatch
    def generate(cls, domain: UUID = None, object_data: str = None) -> Tuple[bool, UUID | str]:
        return False, cls.__get_message_unsupported_error()

    @classmethod
    @generate.register
    def _(cls) -> Tuple[bool, UUID | str]:
        try:
            return True, uuid4()

        except (OSError, NotImplementedError) as e:
            return False, cls.__get_message_system_error(4, e)

        except Exception as e:
            return False, cls.__get_message_unexpected_error(4, e)

    @classmethod
    @generate
    def _(cls, domain: UUID, object_data: str) -> Tuple[bool, UUID | str]:
        try:
            return True, uuid5(namespace=domain, name=object_data)

        except (OSError, NotImplementedError) as e:
            return False, cls.__get_message_system_error(5, e)

        except Exception as e:
            return False, cls.__get_message_unexpected_error(5, e)

    @staticmethod
    def __get_message_unsupported_error() -> str: return 'unsupported arguments'

    @staticmethod
    def __get_message_system_error(uuid_version: int, description: Any) -> str:
        return f'"id" generation (version {uuid_version}) system error: {description}'

    @staticmethod
    def __get_message_unexpected_error(uuid_version: int, description: Any) -> str:
        return f'"id" generation (version {uuid_version}) unexpected error: {description}'
