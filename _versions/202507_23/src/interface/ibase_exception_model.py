from abc import abstractmethod
from abc import ABC
from dataclasses import dataclass

@dataclass
class IBaseExceptionModel(ABC):
    @abstractmethod
    def __get_exception_type(self) -> str: ...

    @abstractmethod
    def __get_timestamp(self) -> str: ...
