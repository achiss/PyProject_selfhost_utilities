from typing import Tuple, List


def base_processing_name_string(*args: str) -> Tuple[bool, str]:
	if len(args) == 0:
		return False, 'at least one value must be passed (no arguments)'
	
	data: List[str] = []
	for i, item in enumerate(args):
		if isinstance(item, str):
			data.append(item)
		
		else:
			try:
				processing_item: str = str(item)
				data.append(processing_item)
			
			except Exception as e:
				return False, f'argument at position {i}, cannot be converted to string: {e}'
	
	return True, ' '.join(data)
