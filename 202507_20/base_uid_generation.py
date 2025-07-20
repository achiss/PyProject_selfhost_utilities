from uuid import UUID
from uuid import uuid5
from typing import Tuple


def processing_args(*args: str) -> Tuple: pass


def base_uid_generation(domain: UUID, *args: str) -> Tuple[bool, UUID | str]:

    try:
        string = processing_args(*args)
        return True, uuid5(namespace = domain, name = string)
    
    except Exception as e:
        pass
