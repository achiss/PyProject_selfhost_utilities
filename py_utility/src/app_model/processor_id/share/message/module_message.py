DATA_TYPE_ERROR: str = 'invalid ID data type - expected "UUID" or "str", got "{}"'

LENGTH_ERROR: str = 'incorrect ID length value - expected "36", got "{}"'

FMT_ERROR_COMMON: str = 'incorrect ID format (not allowed pattern) - {}'

FMT_ERROR_V4: str = 'incorrect ID format (UUID version 4) - {}'

FMT_ERROR_V5: str = 'incorrect ID format (UUID version 5) - {}'

FMT_ERROR_V4_V5: str = 'incorrect ID format (UUID version 4 / 5) - {}'

UNEXPECTED_ERROR: str = 'unexpected error - {}'
