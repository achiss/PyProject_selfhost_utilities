from typing import Any, Type, Tuple


def get_message_empty_list_error(description: str) -> str:
    return f'incorrect {description} list length: cannot be empty (at least one parameter should be defined)'


def get_message_data_type_error(expected_data_type: str, received_data_type: str) -> str:
    return f'invalid argument data type: expected "{expected_data_type}", got "{received_data_type}"'


class ValidatorCommon:
    @staticmethod
    def check_data_type(*data_type: Type[Any], checked_value: Any) -> Tuple[bool, None | str]:
        """
        Args:
            data_type (Type[Any]): expected data types
            checked_value (Any): the value being checked

        Returns:
            - True, None - if success
            - False, message (str) - if failed
        """

        if len(data_type) == 0:
            return False, get_message_empty_list_error(description='data type')

        if any(isinstance(checked_value, argument_data_type) for argument_data_type in data_type):
            return True, None

        else:
            expected_types: str = ', '.join(data_type.__name__ for data_type in data_type)
            received_type: str = str(type(checked_value).__name__)

            return False, get_message_data_type_error(
                expected_data_type=expected_types,
                received_data_type=received_type,
            )
