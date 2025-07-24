from enum import Enum


class ValidateMethod(Enum):
    METHOD_BOTH = None
    METHOD_UUID = 'UUID'
    METHOD_UUID4 = 'UUID4'
    METHOD_UUID5 = 'UUID5'
