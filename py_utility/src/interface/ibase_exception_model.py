from abc import ABC
from typing import Type, Any


class IBaseExceptionModel(ABC, Exception):
    __slots__ = ()

    @staticmethod
    def __get_exception_type(value: Type[Any]) -> str: ...

    @staticmethod
    def __get_timestamp() -> str: ...
