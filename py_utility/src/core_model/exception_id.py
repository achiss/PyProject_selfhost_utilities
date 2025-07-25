from typing import Type, List, Any
from datetime import datetime

from src.core_model.base_model.base_exception_model import BaseExceptionModel


class ExceptionID(BaseExceptionModel):
	def __init__(self, original_exception: Type[Exception], exception_message: str | List[str]) -> None:
		super().__init__(
			custom_exception = self.__get_type_name(ExceptionID),
			original_exception = self.__get_type_name(original_exception),
			exception_message = exception_message,
			exception_timestamp = self.__get_timestamp()
		)

	@staticmethod
	def __get_timestamp() -> str:
		from data.fromat import DATETIME_ISO

		return datetime.now().strftime(format=DATETIME_ISO)

	@staticmethod
	def __get_type_name(exception_type: Type[Any]) -> str: return exception_type.__name__
