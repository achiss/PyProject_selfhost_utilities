from abc import ABC
from abc import abstractmethod
from uuid import UUID


class IProcessorID(ABC):
    __slots__ = ()

    @staticmethod
    @abstractmethod
    def convert(value: str | UUID) -> str | UUID: ...

    @staticmethod
    @abstractmethod
    def generate(*object_data: str, domain: UUID) -> UUID: ...

    @staticmethod
    @abstractmethod
    def validate(value: str | UUID) -> bool: ...
