from dataclasses import dataclass
from datetime import datetime

from src.interface import IBaseExceptionModel


@dataclass(frozen=False, slots=True)
class BaseExceptionModel(Exception, IBaseExceptionModel):
    current_type: str
    original_type: str | None
    message: str
    code: int | None
    timestamp: str

    def __init__(self, original_type: str | None, message: str, code: int | None) -> None:
        self.current_type = self.__get_exception_type()
        self.original_type = original_type
        self.message = message
        self.code = code
        self.timestamp = self.__get_timestamp()

    def __get_exception_type(self) -> str: return self.__class__.__name__

    def __get_timestamp(self) -> str:

        from data.format import DATETIME_ISO

        return datetime.now().strftime(format=DATETIME_ISO)

    def __str__(self) -> str:
        return (f'Exception:\n'
                f' - current type: {self.current_type}\n'
                f' - original type: {self.original_type}\n'
                f' - message: {self.message}\n'
                f' - code: {self.code}\n'
                f' - timestamp: {self.timestamp}')
