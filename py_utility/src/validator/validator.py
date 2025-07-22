from typing import Tuple, Any, Type


class Validator:
    @staticmethod
    def check_data_type(*data_type: Type[Any], checked_value: Any) -> Tuple[bool, None | str]:

        from data.message import get_message_empty_list_error, get_message_data_type_error

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
                expected_data_type=expected_types, received_data_type=received_type,)
