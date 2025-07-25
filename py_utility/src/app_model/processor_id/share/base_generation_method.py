from uuid import UUID
from uuid import uuid4, uuid5


def get_uuid4() -> UUID: return uuid4()


def get_uuid5(domain: UUID, object_data: str) -> UUID: return uuid5(namespace = domain, name = object_data)
