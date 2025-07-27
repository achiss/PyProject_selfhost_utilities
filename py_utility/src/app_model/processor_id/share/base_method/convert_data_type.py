from uuid import UUID


def uuid_to_str(value: UUID) -> str: return str(value)


def str_to_uuid(value: str) -> UUID: return UUID(value)
