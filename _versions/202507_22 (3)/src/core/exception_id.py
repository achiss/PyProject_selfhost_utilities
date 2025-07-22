from typing import Type, Any
from datetime import datetime

class ExceptionID(Exception):
    """
    Custom exception class for ID processing
    """

    __slots__ = ('__message', '__exception_type', '__original_exception_type', '__timestamp')

    def __init__(self, message: str, original_exception_type: Type[Any] | None) -> None:

        self.__message = message
        self.__exception_type = self.__class__.__name__
        self.__original_exception_type = original_exception_type
        self.__timestamp = self.__timestamp()

    @staticmethod
    def __get_timestamp(fmt: str = '%Y-%m-%d %H:%M:%S') -> str: return datetime.now().strftime(format=fmt)

    def __str__(self) -> str:
        return (f'Exception type: {self.__exception_type}\n'
                f'Original exception: {self.__original_exception_type}\n'
                f'Message: {self.__message}\n'
                f'Timestamp: {self.__timestamp}')
