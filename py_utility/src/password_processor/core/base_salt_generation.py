from typing import Tuple, List

from bcrypt import gensalt


def base_salt_processing(iteration_number: int,
                         minimal_range_value: int,
                         maximal_range_value: int,
                         prefix_string: str,
                         encoding_type: str,) -> Tuple[bool, bytes | List[str]]:

    from src.validator import Validator

    error_list: List[str] = []

    for validator in [
        lambda: Validator.check_data_type(value=iteration_number, data_type=int),
        lambda: Validator.check_range_value(
            value=iteration_number, minimal_value=minimal_range_value, maximal_value=maximal_range_value),
    ]:
        flag, message = validator()
        if not flag:
            message: str = f'salt generation failed: {message}'
            error_list.append(message)

    if len(error_list) > 0:
        return False, error_list

    try:
        prefix_string: bytes = prefix_string.encode(encoding=encoding_type)
        salt: bytes = gensalt(rounds=iteration_number, prefix=prefix_string)
        return True, salt

    except UnicodeEncodeError as e:
        return False, [f'salt generation encoding error: {e}']

    except Exception as e:
        return False, [f'salt generation unexpected error: {e}']
