from typing import Tuple
from uuid import UUID
from re import Pattern, IGNORECASE
from re import compile

REGEX_UUID4: Pattern = compile(
    pattern=r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$',
    flags=IGNORECASE
)

REGEX_UUID5: Pattern = compile(
    pattern=r'^[a-f0-9]{8}-[a-f0-9]{4}-5[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$',
    flags=IGNORECASE
)


def verify_uuid(value: str, is_initial: bool) -> Tuple[bool, None | str]:

    if is_initial:
        try:
            flag: bool = bool(REGEX_UUID4.fullmatch(value))
            if flag:
                return True, None

            return False, None

        except Exception as e:
            return False, f'initial UUID verification unexpected error: {e}'
    
    else:
        try:
            flag: bool = bool(REGEX_UUID5.fullmatch(value))
            if flag:
                return True, None
            
            return False, None
        
        except Exception as e:
            return False, f'UUID verification unexpected error: {e}'
