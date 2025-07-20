from typing import Tuple
from typing import overload

from src.core.processing_id.regex import REGEX_UUID4, REGEX_UUID5


@overload
def verify_uuid(value: str, is_initial: bool) -> Tuple[bool, None | str]: ...

@overload
def verify_uuid(value: str) -> Tuple[bool, None | str]: ...

def verify_uuid(value: str = None,
                is_initial: bool = False) -> Tuple[bool, None | str]:

    if is_initial:
        try:
            flag: bool = bool(REGEX_UUID4.fullmatch(value))
            if flag:
                return True, None

            return False, 'is not a valid UUID'

        except Exception as e:
            return False, f'initial UUID verification unexpected error: {e}'
    
    else:
        try:
            flag: bool = bool(REGEX_UUID5.fullmatch(value))
            if flag:
                return True, None
            
            return False, 'is not a valid UUID'
        
        except Exception as e:
            return False, f'UUID verification unexpected error: {e}'
