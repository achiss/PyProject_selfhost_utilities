from typing import List

from src.password_processor.core.base_salt_generation import base_salt_processing
from src.password_processor.core.base_password_encoding import base_password_hashing


class PasswordProcessor:
    @staticmethod
    def hashing_password(password_string: str, iteration_number: int, minimal_range_value: int,
                         maximal_range_value: int) -> bytes:

        from src.validator import Validator

        try:
            error_list: List[str] = []
            for validator in [
                lambda: Validator.check_data_type(value=minimal_range_value, data_type=int),
                lambda: Validator.check_data_type(value=maximal_range_value, data_type=int),
                lambda: Validator.check_range_value(value=iteration_number, minimal_value=minimal_range_value, maximal_value=maximal_range_value)
            ]:
                flag, message = validator()
                if not flag:
                    error_list.append(message)

            if len(error_list) > 1:
                raise ValueError(message)

            flag, expected_value = base_salt_processing()
            if not flag:
                raise RuntimeError(expected_value)

            flag, expected_value = base_password_hashing()
            if not flag:
                raise RuntimeError(expected_value)

            return expected_value

        except ValueError as e:
            raise ValueError(f'Password processor - parameter error: {e}')

        except RuntimeError as e:
            raise RuntimeError(f'Password processor error: {e}')

        except Exception as e:
            raise Exception(f'Password processor - unexpected error: {e}') from e
