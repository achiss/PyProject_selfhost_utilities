from uuid import UUID
from uuid import uuid4, uuid5

from data import REGEX_UUID4, REGEX_UUID5


def get_uuid4() -> UUID: return uuid4()


def get_uuid5(domain: UUID, object_string: str) -> UUID: return uuid5(namespace=domain, name=object_string)


def check_uuid4(uuid_number: str) -> bool: return bool(REGEX_UUID4.fullmatch(string=uuid_number))


def check_uuid5(uuid_number: str) -> bool: return bool(REGEX_UUID5.fullmatch(string=uuid_number))
