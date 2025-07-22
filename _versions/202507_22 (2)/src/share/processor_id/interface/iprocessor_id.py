from typing import Protocol
from uuid import UUID


class IProcessorID(Protocol):
    @classmethod
    def generate(cls, domain: UUID = None, *args: str | bytes) -> UUID: ...

    @classmethod
    def validate(cls, uid_number: str | UUID) -> bool: ...

    @classmethod
    def convert(cls, uid_number: UUID) -> str: ...
