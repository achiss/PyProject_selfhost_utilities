from uuid import UUID
from typing import Tuple
from typing import overload

from src.utility.id.base_method.base_id_generation import base_id_generation
from src.utility.id.base_method.base_processing_domain import base_processing_domain
from src.utility.id.base_method.base_processing_name_string import base_processing_name_string


class ID:
	@classmethod
	@overload
	def generate(cls) -> Tuple[bool, None | str]: ...
	
	@classmethod
	@overload
	def generate(cls, domain: UUID | str, *name_string: str) -> Tuple[bool, None | str]: ...
	
	@classmethod
	def generate(cls, domain: UUID | str = None, *name_string: str) -> Tuple[bool, None | str]:
		from src.validator.general_verification import verify_data_type
		from src.validator.uid_verification import verify_uuid

		if not domain:
			pass
		
		flag, domain_data = base_processing_domain(domain)
		if not flag:
			raise Exception(f'invalid domain: {domain_data}')

		flag, name_string_data = base_processing_name_string(*name_string)
		if not flag:
			raise Exception(f'invalid name: {name_string_data}')
		
		return base_id_generation(domain_data, name_string_data)
		
