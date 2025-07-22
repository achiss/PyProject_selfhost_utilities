def get_message_empty_list_error(description: str) -> str:
    return f'incorrect {description} list length: cannot be empty (at least one parameter should be defined)'


def get_message_data_type_error(expected_data_type: str, received_data_type: str) -> str:
    return f'invalid argument data type: expected "{expected_data_type}", got "{received_data_type}"'
