from typing import Any, Type, Tuple


def verify_data_type(value_check: Any,
                     *args: Type[Any]) -> Tuple[bool, None | str]:

    """
    Args:
        value_check: the value being checked
        args: expected data types

    Returns:
        - True, None - if success
        - False, message (str) - if failed
    """

    if len(args) == 0:
        return False, 'the data types should be defined'

    if any(isinstance(value_check, data_type) for data_type in args):
        return True, None

    else:
        expected_types: str = ', '.join(data_type.__name__ for data_type in args)
        received_type: type = type(value_check).__name__
        return False, f'invalid data type value > expected: {expected_types}, got: {received_type}'


def verify_length(value_length: int | float,
                  required_length: int | float) -> Tuple[bool, None | str]:
    """
    Args:
        value_length: the value being checked
        required_length: expected length (expected: int or float)

    Returns:
        - True, None - if success
        - False, message (str) - if failed
    """

    if value_length == required_length:
        return True, None

    return False, f'incorrect length > values must be equal, got: {value_length} not equal to {required_length}'


def verify_length_less(value_length: int | float,
                       required_length: int | float,
                       is_equal: bool = False) -> Tuple[bool, None | str]:

    """
    Args:
        value_length: the value being checked
        required_length: expected length (expected: int or float)
        is_equal: If you need to check the equality (default: False)

    Returns:
        - True, None - if success
        - False, message (str) - if failed
    """

    if is_equal and value_length <= required_length:
        return True, None

    elif not is_equal and value_length < required_length:
        return True, None

    else:
        return False, (f'incorrect length > value must be equal to or less, got {value_length} not equal or less to {required_length}'
                       if is_equal else
                       f'incorrect length > value must be less, got {value_length} not less to {required_length}')



def verify_length_greater(value_length: int | float,
                          required_length: int | float,
                          is_equal: bool = False) -> Tuple[bool, None | str]:
    """
    Args:
        value_length: the value being checked
        required_length: expected length (expected: int or float)
        is_equal: If you need to check the equality (default: False)

    Returns:
        - True, None - if success
        - False, message (str) - if failed
    """

    if is_equal and value_length >= required_length:
        return True, None

    elif not is_equal and value_length > required_length:
        return True, None

    else:
        return False, (f'incorrect length > value must be equal to or greater, got {value_length} not equal or greater to {required_length}'
                       if is_equal else
                       f'incorrect length > value must be greater, got {value_length} not greater to {required_length}')


def check_lower_limit(value_length: int | float,
                      minimal_range_value: int | float,
                      minimal_value_as_equal: bool) -> bool:

    if minimal_value_as_equal:
        result: bool = value_length >= minimal_range_value

    else:
        result: bool = value_length > minimal_range_value

    if not result:
        return False

    return True


def check_upper_limit(value_length: int | float,
                      maximal_range_value: int | float,
                      maximal_value_as_equal: int | float) -> bool:

    if maximal_value_as_equal:
        result: bool = value_length <= maximal_range_value

    else:
        result: bool = value_length < maximal_range_value

    if not result:
        return False

    return True


def verify_range(value_length: int | float,
                 minimal_range_value: int | float,
                 maximal_range_value: int | float,
                 minimal_value_as_equal: bool = False,
                 maximal_value_as_equal: bool = False) -> Tuple[bool, None | str]:

    """
    Args:
        value_length: the value being checked
        minimal_range_value: the lower limit of the range
        maximal_range_value: the upper limit of the range
        minimal_value_as_equal: if True, it includes the lower limit in the range (>=) (default: False)
        maximal_value_as_equal: if True, it includes the upper limit in the range (<=) (default: False)

    Returns:
        - True, None - if success
        - False, message (str) - if failed
    """

    if minimal_value_as_equal > maximal_value_as_equal:
        return False, f'incorrect range parameter > minimal value cannot be greater than maximal value'

    lower_check: bool = check_lower_limit(value_length, minimal_range_value, minimal_value_as_equal)
    if not lower_check:
        message: str = (f'incorrect range parameter > checked value is less than '
                        f'{'or equal' if minimal_value_as_equal else ''}minimal allowed "{minimal_range_value}"')
        return False, message

    upper_check: bool = check_upper_limit(value_length, maximal_range_value, maximal_value_as_equal)
    if not upper_check:
        message: str = (f'incorrect range parameter > checked value is greater than '
                        f'{'or equal' if maximal_value_as_equal else ''}maximal allowed "{maximal_range_value}"')
        return False, message

    return True, None


if __name__ == '__main__':
    pass
