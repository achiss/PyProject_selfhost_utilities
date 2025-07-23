from typing import Type, Any
from datetime import datetime

from src.interface import IBaseExceptionModel


class BaseExceptionModel(IBaseExceptionModel):
    __slots__ = ('__custom_type', '__original_type', '__message', '__code', '__timestamp')

    def __init__(self, custom_type: Type[Any], original_type: Type[Any] | None, message: str, code: int | None) -> None:
        self.__custom_type = self.__get_exception_type(custom_type)
        self.__original_type = self.__get_exception_type(original_type)
        self.__message = message
        self.__code = code
        self.__timestamp = self.__get_timestamp()

    @property
    def custom_type(self) -> str: return self.__custom_type

    @property
    def original_type(self) -> str | None: return self.__original_type

    @property
    def message(self) -> str: return self.__message

    @property
    def code(self) -> int | None: return self.__code

    @property
    def timestamp(self) -> str: return self.__timestamp

    @staticmethod
    def __get_exception_type(value: Type[Any]) -> str: return value.__name__

    @staticmethod
    def __get_timestamp() -> str:
        from data.format.datetime_fmt import DATETIME_ISO

        return datetime.now().strftime(format=DATETIME_ISO)

    def __str__(self) -> str:
        return (f'Exception data:\n'
                f' - custom exception type: {self.custom_type}\n'
                f' - original exception type: {self.original_type}\n'
                f' - exception message: {self.message}\n'
                f' - exception code: {self.code}\n'
                f' - timestamp: {self.timestamp}')
