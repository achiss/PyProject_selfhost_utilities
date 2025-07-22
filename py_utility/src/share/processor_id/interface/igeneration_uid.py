from typing import Protocol, Tuple
from typing import overload
from uuid import UUID


class IGenerationUid(Protocol):
    @classmethod
    @overload
    def generate(cls) -> Tuple[bool, UUID | str]: ...

    @classmethod
    @overload
    def generate(cls, domain: UUID, object_data: str) -> Tuple[bool, UUID | str]: ...

    @classmethod
    def generate(cls, domain: UUID = None, object_data: str = None) -> Tuple[bool, UUID | str]: ...
