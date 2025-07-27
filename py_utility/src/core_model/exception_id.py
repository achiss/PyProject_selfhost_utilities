from typing import Type

from src.core_model.base_model.base_exception_model import BaseExceptionModel


def get_exception_name(value: Type[Exception]) -> str: return value.__name__


class ExceptionID(BaseExceptionModel):
	__slots__ = ()
	
	def __init__(self, original_exception_type: Type[Exception], exception_message: str) -> None:
		super().__init__(
			custom_exception_type = get_exception_name(ExceptionID),
			original_exception_type = get_exception_name(original_exception_type),
			exception_message = exception_message,
		)
