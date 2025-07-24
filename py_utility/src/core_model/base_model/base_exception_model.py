from typing import Type
from datetime import datetime

from src.interface import BaseExceptionModelProtocol


class BaseExceptionModel(BaseExceptionModelProtocol, Exception):
	__slots__ = ('__custom_exception', '__original_exception', '__exception_message', '__exception_timestamp')
	
	def __init__(self, custom_exception: Type[Exception], original_exception: Type[Exception],
	             exception_message: str) -> None:

		self.__custom_exception = self.__get_exception_name(custom_exception)
		self.__original_exception = self.__get_exception_name(original_exception)
		self.__exception_message = exception_message
		self.__exception_timestamp = self.__get_timestamp()
	
	@staticmethod
	def __get_exception_name(exception_type: Type[Exception]) -> str: return exception_type.__name__
	
	@staticmethod
	def __get_timestamp() -> str: return datetime.now().isoformat()
	
	def __str__(self) -> str:
		return (f'\n---------\n'
		        f'Custom Exception: {self.__custom_exception}\n'
		        f'Original Exception: {self.__original_exception}\n'
		        f'Exception Message: {self.__exception_message}\n'
		        f'Exception Timestamp: {self.__exception_timestamp}\n'
		        f'---------')


if __name__ == '__main__':
	pass
