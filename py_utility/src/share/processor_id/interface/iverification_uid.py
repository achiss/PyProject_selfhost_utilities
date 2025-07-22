from typing import Protocol, Tuple
from typing import overload
from uuid import UUID


class IVerificationUid(Protocol):
    @classmethod
    @overload
    def validate(cls, uid_number: str) -> Tuple[bool, None | str]: ...

    @classmethod
    @overload
    def validate(cls, uid_number: UUID) -> Tuple[bool, None | str]: ...

    @classmethod
    def validate(cls, uid_number: str | UUID = None) -> Tuple[bool, None | str]: ...
