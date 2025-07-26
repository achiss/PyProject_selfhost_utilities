from typing import Type, List, Any
from datetime import datetime

from src.core_model.base_model.base_exception_model import BaseExceptionModel


class ExceptionID(BaseExceptionModel):
	__slots__ = ('__raw_type', '__raw_message',)

	def __init__(self, original_exception: Type[Exception], exception_message: str | List[str]) -> None:
		super().__init__()
		
		object.__setattr__(self, '__raw_type', original_exception)
		object.__setattr__(self, '__raw_message', exception_message)
	
	def __post_init__(self) -> None:
		object.__setattr__(self, 'custom_exception', self.__get_type_name(type(self)))
		object.__setattr__(self, 'original_exception', self.__get_type_name(self.__raw_type))
		object.__setattr__(self, 'exception_message', self.__raw_message)
		object.__setattr__(self, 'exception_timestamp', self.__get_timestamp())

	@staticmethod
	def __get_timestamp() -> str:
		from data.format import DATETIME_ISO

		return datetime.now().strftime(format=DATETIME_ISO)

	@staticmethod
	def __get_type_name(exception_type: Type[Any]) -> str: return exception_type.__name__
