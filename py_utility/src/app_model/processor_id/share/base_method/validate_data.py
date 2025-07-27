from uuid import UUID

from data.pattern import REGEX_UUID, REGEX_UUID4, REGEX_UUID5


def check_id_type(value: UUID | str) -> bool: return bool(isinstance(value, (UUID, str)))


def check_id_length(value: UUID | str) -> bool: return len(value) == 36


def check_uuid(value: str) -> bool: return bool(REGEX_UUID.fullmatch(value))


def check_uuid_v4(value: UUID | str) -> bool: return bool(REGEX_UUID4.fullmatch(value))


def check_uuid_v5(value: UUID | str) -> bool: return bool(REGEX_UUID5.fullmatch(value))
