from typing import Type, Any
from datetime import datetime

from src.interface import IBaseExceptionModel


class BaseExceptionModel(IBaseExceptionModel):
    __slots__ = ('__custom_type', '__original_type', '__message', '__timestamp')

    def __init__(self, custom_type: Type[Any], original_type: Type[Any] | None, message: str) -> None:
        self.__custom_type = self.__get_exception_type(custom_type)
        self.__original_type = self.__get_exception_type(original_type)
        self.__message = message
        self.__timestamp = self.__get_timestamp()

    @property
    def custom_type(self) -> str: return self.__custom_type

    @custom_type.setter
    def custom_type(self, value: Type[Any]) -> None: self.__custom_type = self.__get_exception_type(value)

    @property
    def original_type(self) -> str | None: return self.__original_type

    @property
    def message(self) -> str: return self.__message

    @property
    def timestamp(self) -> str: return self.__timestamp

    @staticmethod
    def __get_exception_type(value: Type[Any]) -> str: return value.__name__

    @staticmethod
    def __get_timestamp() -> str:
        from data.format.datetime_fmt import DATETIME_ISO

        return datetime.now().strftime(format=DATETIME_ISO)

    def __str__(self) -> str:
        return (f'\n---------\n'
                f'Exception data:\n'
                f' - custom exception type: {self.custom_type}\n'
                f' - original exception type: {self.original_type}\n'
                f' - exception message: {self.message}\n'
                f' - timestamp: {self.timestamp}\n'
                f'---------\n')
