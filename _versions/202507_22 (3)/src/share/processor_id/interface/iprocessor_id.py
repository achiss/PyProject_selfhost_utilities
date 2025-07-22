from typing import Protocol
from uuid import UUID


class IProcessorID(Protocol):
    @staticmethod
    def generate(*object_string: str | None, domain: UUID | None = None) -> UUID: ...

    @staticmethod
    def validate(uuid_number: str | UUID) -> bool: ...

    @staticmethod
    def convert(uuid_number: str | UUID) -> str: ...
