from typing import Tuple, Type, Any


def check_data_type(checked_value: Any,
                    reference_data_type: Type[Any]) -> Tuple[bool, str | None, Type[Exception] | None]:

    from src.share.verify.message.message_data_type import from_data_type
    from src.share.verify.message.message_unexpected import from_unexpected

    try:
        if not isinstance(checked_value, reference_data_type):
            _message: str = from_data_type(
                checked_data_type = type(checked_value),
                reference_data_type = reference_data_type,
            )
            return False, _message, TypeError

        return True, None, None

    except Exception as e:
        _message: str = from_unexpected(
            description = str(e),
        )
        return False, _message, type(e)


def check_data_types(*reference_data_types: Type[Any],
                     checked_value: Any) -> Tuple[bool, str | None, Type[Exception] | None]:

    from src.share.verify.message.message_data_type import from_data_type
    from src.share.verify.message.message_unexpected import from_unexpected
    from src.share.verify.message.message_length import from_length_equal

    try:
        if len(reference_data_types) == 0:
            _message: str = from_length_equal(
                checked_length = len(reference_data_types),
                reference_length = 0,
            )
            return False, _message, ValueError

        if not any(isinstance(checked_value, _t) for _t in reference_data_types):
            _expected_types: str = ', '.join(_t.__name__ for _t in reference_data_types)
            _message: str = from_data_type(
                checked_data_type=type(checked_value),
                reference_data_type=_expected_types,
            )
            return False, _message, TypeError

        return True, None, None

    except Exception as e:
        _message: str = from_unexpected(
            description = str(e),
        )
        return False, _message, type(e)
