from typing import Protocol, Type


class BaseExceptionModelProtocol(Protocol):
	__slots__ = ()

	@staticmethod
	def __get_timestamp() -> str: ...
	
	@staticmethod
	def __get_exception_name(exception_type: Type[Exception]) -> str: ...
