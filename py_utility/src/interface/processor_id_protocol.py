from typing import Protocol, Any
from uuid import UUID

from src.app_model.process_id.share.validate_method import ValidateMethod


class ProcessorIDProtocol(Protocol):
    @staticmethod
    def convert(uuid_value: UUID | str) -> UUID | str: ...

    @staticmethod
    def generate(*object_data: Any, domain: UUID | None = None) -> UUID: ...

    @staticmethod
    def validate(uuid_value: UUID | str, validate_method: 'ValidateMethod') -> UUID | str: ...
