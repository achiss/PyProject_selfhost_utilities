from functools import singledispatch
from typing import Tuple, Any
from uuid import UUID

from src.share.processor_id.interface import IVerificationUid

from data.instruction import REGEX_UUID4, REGEX_UUID5


class VerificationUid(IVerificationUid):
    @classmethod
    @singledispatch
    def validate(cls, uid_number: str | UUID = None) -> Tuple[bool, None | str]:
        return False, cls.__get_message_unsupported_error()

    @classmethod
    @validate.register
    def _(cls, uid_number: str) -> Tuple[bool, None | str]:
        try:
            if cls.__verify_regex_uuid4(uid_number) or cls.__verify_regex_uuid5(uid_number):
                return True, None

            return False, None

        except Exception as e:
            return False, cls.__get_message_unexpected_error(e)

    @classmethod
    @validate.register
    def _(cls, uid_number: UUID) -> Tuple[bool, None | str]:
        try:
            uid_number: str = str(uid_number)
            if cls.__verify_regex_uuid4(uid_number) or cls.__verify_regex_uuid5(uid_number):
                return True, None

            return False, None

        except Exception as e:
            return False, cls.__get_message_unexpected_error(e)

    @staticmethod
    def __get_message_unsupported_error() -> str: return 'unsupported arguments'

    @staticmethod
    def __get_message_unexpected_error(description: Any) -> str:
        return f'"id" validation unexpected error: {description}'

    @staticmethod
    def __verify_regex_uuid4(uid_number: str) -> bool: return bool(REGEX_UUID4.fullmatch(uid_number))

    @staticmethod
    def __verify_regex_uuid5(uid_number: str) -> bool: return bool(REGEX_UUID5.fullmatch(uid_number))
