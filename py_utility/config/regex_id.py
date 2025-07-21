from re import Pattern, IGNORECASE
from re import compile


REGEX_UID4: Pattern = compile(
    pattern=r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$',
    flags=IGNORECASE
)

REGEX_UID5: Pattern = compile(
    pattern=r'^[a-f0-9]{8}-[a-f0-9]{4}-5[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$',
    flags=IGNORECASE
)
