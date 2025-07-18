from typing import Tuple, List

from bcrypt import hashpw


def base_password_hashing(password_string: str,
                          salt: bytes,
                          password_length_required: int,
                          encoding_type: str) -> Tuple[bool, bytes | List[str]]:

    from src.validator import Validator

    error_list: List[str] = []

    for validator in [
        lambda: Validator.check_data_type(value=password_string, data_type=str),
        lambda: Validator.check_length_less(value=len(password_string), reference_value=password_length_required)
    ]:
        flag, message = validator()
        if not flag:
            message: str = f'password hash generation failed: {message}'
            error_list.append(message)

    if len(error_list) > 0:
        return False, error_list

    try:
        password: bytes = password_string.encode(encoding=encoding_type)
        password: bytes = hashpw(password=password, salt=salt)
        return True, password

    except UnicodeEncodeError as e:
        return False, [f'password hash generation encoding error: {e}']

    except Exception as e:
        return False, [f'password hash generation unexpected error: {e}']
