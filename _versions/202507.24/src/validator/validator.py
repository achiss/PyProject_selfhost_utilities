from typing import Tuple, Any, Type


class Validator:
    @staticmethod
    def check_data_type(*data_type: Type[Any], checked_value: Any) -> Tuple[bool, None | str, Type[Any] | None]:

        """
        Args:
            data_type (Type[Any]): expected data types
            checked_value (Any): the value being checked

        Returns:
            - True, None, None - if success
            - False, message (str), error type - if false
        """

        if len(data_type) == 0:
            _message: str = f'list of data type(s) should be defined'
            return False, _message, ValueError

        if any(isinstance(checked_value, argument_data_type) for argument_data_type in data_type):
            return True, None, None

        else:
            expected_types: str = ', '.join(data_type.__name__ for data_type in data_type)
            received_type: str = str(type(checked_value).__name__)

            _message: str = f'invalid data type: expected "{expected_types}", got "{received_type}"'
            return False, _message, TypeError

    @staticmethod
    def check_length_equal(value_length: int, required_length: int) -> Tuple[bool, None | str, Type[Any] | None]:

        """
        Args:
              value_length (int): checked value
              required_length(int): reference length value

        Returns:
            - True, None, None - if success
            - False, message (str), error type - if false
        """

        if value_length == required_length:
            return True, None, None

        else:
            _message: str = f'incorrect length value: expected length "{required_length}", got length "{value_length}"'
            return False, _message, ValueError

    @staticmethod
    def check_length_less(value_length: int, reference_length: int,
                          is_equal: bool = False) -> Tuple[bool, None | str, Type[Any] | None]:

        """
        Args:
            value_length (int): checked value
            reference_length (int): reference length value
            is_equal (bool): if include a value in the range - True, otherwise - False (default: False)

        Returns:
            - True, None, None - if success
            - False, message (str), error type - if false
        """

        _result: bool = (value_length < reference_length) or (is_equal and value_length == reference_length)
        if _result:
            return True, None, None

        else:
            if is_equal:
                _message: str = (f'incorrect length value: expected length "{value_length}" should be less or equal '
                                 f'to "{reference_length}"')

            else:
                _message: str = (f'incorrect length value: expected length "{value_length}" should be less '
                                 f'to "{reference_length}"')

            return False, _message, ValueError

    @staticmethod
    def check_length_greater(value_length: int, reference_length: int,
                             is_equal: bool = False) -> Tuple[bool, None | str, Type[Any] | None]:

        """
        Args:
            value_length (int): checked value
            reference_length (int): reference length value
            is_equal (bool): if include a value in the range - True, otherwise - False (default: False)

        Returns:
            - True, None, None - if success
            - False, message (str), error type - if false
        """

        _result: bool = (value_length > reference_length) or (is_equal and value_length == reference_length)
        if _result:
            return True, None, None

        else:
            if is_equal:
                _message: str = (f'incorrect length value: expected length "{value_length}" should be greater or equal '
                                 f'to "{reference_length}"')

            else:
                _message: str = (f'incorrect length value: expected length "{value_length}" should be greater '
                                 f'to "{reference_length}"')

            return False, _message, ValueError
