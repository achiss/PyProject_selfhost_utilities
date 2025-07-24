from enum import Enum


class ValidateMethod(Enum):
    METHOD_BOTH: None = None
    METHOD_UUID: str = 'UUID'
    METHOD_UUID4: str = 'UUID4'
    METHOD_UUID5: str = 'UUID5'
