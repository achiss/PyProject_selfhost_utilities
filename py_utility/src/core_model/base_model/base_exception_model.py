from dataclasses import dataclass, field
from datetime import datetime

from src.interface import IBaseExceptionModel


@dataclass(frozen = True, slots = True)
class BaseExceptionModel(IBaseExceptionModel):
	custom_exception_type: str
	original_exception_type: str
	exception_message: str
	exception_timestamp: str = field(default = datetime.now().strftime(format = '%Y-%m-%d %H:%M:%S'))
	
	def __str__(self) -> str:
		return (f'\n---------\n'
		        f'Exception type: {self.custom_exception_type}\n'
		        f'Original exception type: {self.original_exception_type}\n'
		        f'Exception message: {self.exception_message}\n'
		        f'Exception timestamp: {self.exception_timestamp}\n'
		        f'---------\n')
	