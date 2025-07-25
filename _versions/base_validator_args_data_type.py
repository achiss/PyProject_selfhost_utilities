from typing import Any, Tuple, Type, List


def check_args_data_type(*args: Any, **kwargs: Type[Any]) -> Tuple[bool, str | None, Type[Exception] | None]:

    if len(args) == 0:
        _message = f'incorrect list of values data type - is empty, should be defined'
        return False, _message, ValueError

    if len(kwargs) == 0:
        _message = f'no types provided for validation'
        return False, _message, ValueError

    _allowed_types = tuple(kwargs.values())
    if not all(isinstance(t, type) for t in _allowed_types):
        _message = f'kwargs should be contained types'
        return False, _message, ValueError

    errors_list: List[str] = []
    for count, arg in enumerate(args):
        if not isinstance(arg, _allowed_types):
            _expected_types = ', '.join(t.__name__ for t in _allowed_types)
            _actual_type = type(arg).__name__

            _message = f'invalid argument number "{count}" data type: expected "{_expected_types}", got "{_actual_type}"'
            errors_list.append(_message)

    if len(errors_list) > 0:
        return False, '; '.join(errors_list), TypeError

    return True, None, None