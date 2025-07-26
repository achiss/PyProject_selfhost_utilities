from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True, slots=True)
class BaseExceptionModel(Exception):
	custom_exception: str = field(default = None)
	original_exception: str = field(default = None)
	exception_message: str | List[str] = field(default = None)
	exception_timestamp: str = field(default = None)

	def __str__(self) -> str:
		return (f'\n---------\n'
				f'Exception type: {self.custom_exception}\n'
				f'Original exception type: {self.original_exception}\n'
				f'Message: {BaseExceptionModel.__generate_message(self.exception_message)}\n'
				f'Timestamp: {self.exception_timestamp}\n'
				f'---------\n')

	@staticmethod
	def __generate_message(message: str | List[str]) -> str:
		if isinstance(message, str):
			return message

		elif isinstance(message, list):
			return ''.join(f'\n- {line}' for line in message)

		else:
			return str(message)


if __name__ == '__main__':
	print(BaseExceptionModel())