from uuid import UUID
from uuid import uuid4
from typing import Tuple


def initial_uid_generation() -> Tuple[bool, UUID | str]:

    try:
        return True, uuid4()

    except (OSError, NotImplementedError) as e:
        return False, f'UUID generation failed: {e}'
