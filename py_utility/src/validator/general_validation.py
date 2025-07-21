from typing import Tuple, Type, Any


class GeneralValidation:
    @staticmethod
    def check_data_type(value: Any, *value_type: Type[Any]) -> Tuple[bool, None | str]:
        """
        Args:
            value (Any): the value being checked
            value_type (Type[Any]): expected data types

        Returns:
            - True, None - if success
            - False, message (str) - if failed
        """

        if len(value_type) == 0:
            return False, 'parameter (value data type) should be defined'

        if any(isinstance(value, data_type) for data_type in value_type):
            return True, None

        else:
            expected_types: str = ', '.join(data_type.__name__ for data_type in value_type)
            received_type: type = type(value).__name__
            return False, f'invalid data type value > expected: {expected_types}, got: {received_type}'
