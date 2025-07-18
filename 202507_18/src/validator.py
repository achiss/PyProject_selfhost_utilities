from typing import Tuple, Any, Type, List
from typing import overload


class Validator:
    @staticmethod
    @overload
    def check_data_type(value: Any, data_type: Type) -> Tuple[bool, None | str]: ...

    @staticmethod
    @overload
    def check_data_type(value: Any, first_data_type: Type, second_data_type: Type) -> Tuple[bool, None | str]: ...

    @staticmethod
    def check_data_type(value: Any = None,
                        data_type: Type = None,
                        first_data_type: Type = None,
                        second_data_type: Type = None) -> Tuple[bool, None | str]:

        if data_type:
            message: str = f'invalid data type - expected {data_type}, got {type(value).__name__}'
            if not isinstance(value, data_type):
                return False, message

        else:
            message: str = f'incorrect arguments value, all arguments should be defined'
            if not (first_data_type or second_data_type):
                return False, message

            message: str = (f'invalid data type - expected "{first_data_type}" or "{second_data_type}", '
                            f'got {type(value).__name__}')
            if not isinstance(value, (first_data_type, second_data_type)):
                return False, message

        return True, None

    @staticmethod
    def __check_same_digital_type(first_value: int | float, second_value: int | float) -> Tuple[bool, None | str]:

        message: str = (f'incorrect arguments value - arguments should be of the same type, '
                        f'got "{type(first_value).__name__}" and "{type(second_value).__name__}"')
        if type(first_value) != type(second_value):
            return False, message

        return True, None

    @staticmethod
    def check_length_equal(value: int | float, reference_value: int | float) -> Tuple[bool, None | str]:

        flag, message = Validator.__check_same_digital_type(value, reference_value)
        if not flag:
            return False, message

        message: str = f'parameter values should be equal'
        if value != reference_value:
            return False, message

        return True, None

    @staticmethod
    def check_length_less(value: int | float, reference_value: int | float) -> Tuple[bool, None | str]:

        message: str = f'parameter cannot be less than the reference value'
        if value < reference_value:
            return False, message

        return True, None

    @staticmethod
    def check_range_value(value: int | float,
                    minimal_value: int | float, maximal_value: int | float) -> Tuple[bool, None | str]:

        message: str = f'parameter value must be in the range from "{minimal_value}" to "{maximal_value}"'
        if value < minimal_value:
            return False, message

        elif value > maximal_value:
            return False, message

        return True, None

    @staticmethod
    def check_allowed_list(value: Any, allowed_list: List[Any]) -> Tuple[bool, None | str]:

        message: str = f'parameter value being checked should be allowed'
        if not value in allowed_list:
            return False, message

        return True, None
