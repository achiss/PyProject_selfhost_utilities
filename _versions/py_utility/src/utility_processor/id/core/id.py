from typing import List
from typing import overload
from uuid import UUID


class ID:
	@classmethod
	@overload
	def generate(cls, exception_type: callable) -> UUID: ...

	@classmethod
	@overload
	def generate(cls, exception_type: callable, domain: UUID, *object_string: str | bytes) -> UUID: ...

	@classmethod
	def generate(cls, exception_type: callable, domain: UUID = None, *object_string: str | bytes) -> UUID: pass

	@classmethod
	def to_string(cls, exception_type: callable, id_number: UUID) -> str:

		try:
			return str(id_number)

		except Exception as e:
			raise exception_type(f'ID processing, unexpected error: {e}') from e

	@classmethod
	def verify(cls, exception_type: callable, id_number: str, is_initial: bool) -> bool:

		from src.validator.uid_verification import verify_uuid

		try:
			flag, data =  verify_uuid(value=id_number, is_initial=is_initial)
			if not (flag and data):
				raise RuntimeError(data)

			return flag

		except RuntimeError as e:
			raise exception_type(f'ID processing, verification failed: {e}')

		except Exception as e:
			raise exception_type(f'ID processing, unexpected error: {e}') from e
