from uuid import UUID


def check_id_type(value: UUID | str) -> bool: return bool(isinstance(value, (UUID, str)))


def check_id_length(value: UUID | str) -> bool: return len(value) == 36
