from typing import Type

from src.core_model.base_model.base_exception_model import BaseExceptionModel


class ExceptionID(BaseExceptionModel):
	def __init__(self, original_exception: Type[Exception], exception_message: str) -> None:
		super().__init__(
			custom_exception = ExceptionID,
			original_exception = original_exception,
			exception_message = exception_message,
		)
