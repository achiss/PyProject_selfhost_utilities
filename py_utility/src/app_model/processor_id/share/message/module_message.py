#


#
DATA_TYPE_ERROR: str = 'invalid ID data type - expected "UUID" or "str", got "{}"'

UNEXPECTED_ERROR: str = 'unexpected error - {}'

SYSTEM_ERROR: str = 'system error during generate ID "{}" - {}'


# SECTION: LENGTH
LENGTH_ID_ERROR: str = 'incorrect ID length value - expected "36", got "{}"'

LENGTH_ERROR_EQUAL: str = 'incorrect length value - expected "{}", got "{}"'

LENGTH_ERROR_LESS: str = 'incorrect length value - expected "{}" value should be less than got "{}" value'

LENGTH_ERROR_LESS_EQUAL: str = 'incorrect length value - expected "{}" value should be less or equal than got "{}" value'

LENGTH_ERROR_GREATER: str = 'incorrect length value - expected "{}" value should be greater than got "{}" value'

LENGTH_ERROR_GREATER_EQUAL: str = 'incorrect length value - expected "{}" value should be greater or equal than got "{}" value'

LIST_LENGTH_ERROR: str = 'incorrect "object data" list length value - cannot be empty'

WHITESPACE_EMPTY_ERROR: str = 'incorrect "object_data" value - cannot be empty or whitespace'


# SECTION: FORMAT
FMT_ERROR_COMMON: str = 'incorrect ID format (not allowed pattern) - {}'

FMT_ERROR: str = 'incorrect ID format "{}" - {}'
