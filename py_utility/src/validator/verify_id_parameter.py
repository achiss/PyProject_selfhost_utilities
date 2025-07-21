from typing import Tuple, List
from uuid import UUID


def verify_id_parameter(domain: UUID, *object_string: str) -> Tuple[bool, None | str]:

    from src.validator.general_validation import GeneralValidation

    error_list: List[str] = []

    # NOTE: verify domain
    if not (processing_data := GeneralValidation.check_data_type(domain, UUID))[0]:
        error_list.append(processing_data[1])

    # NOTE: verify object_string
    for i, string in enumerate(object_string, start=1):
        for validator in [
            lambda: GeneralValidation.check_data_type(string, str),
        ]:
            flag, message = validator()
            if not flag:
                error_list.append(f'sequence number {i} - {message}')

    return (True, None) if len(error_list) == 0 else (False, ', '.join(error_list))
