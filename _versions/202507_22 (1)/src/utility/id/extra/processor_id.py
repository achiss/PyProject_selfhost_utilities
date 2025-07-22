from typing import List
from typing import overload
from uuid import UUID
from uuid import uuid4, uuid5

from src.core.exception_id import ExceptionID
from src.validator.verify_id_parameter import verify_id_parameter


class ProcessorID:
    __slots__ = ()

    @classmethod
    @overload
    def generate(cls) -> UUID: ...

    @classmethod
    @overload
    def generate(cls, domain: UUID, *object_string: str | bytes) -> UUID: ...

    @classmethod
    def generate(cls, domain: UUID = None, *object_string: str | bytes) -> UUID:

        try:
            if not domain:
                return uuid4()

            else:
                if not (data := verify_id_parameter(domain, *object_string))[0]:
                    raise RuntimeError(data[1])

                name_string: List[str] = []
                for name_part in object_string:
                    name_string.append(name_part)

                name_string: str = ' '.join(name_string)

                return uuid5(namespace=domain, name=name_string)

        except RuntimeError as e:
            raise ExceptionID(f'ID generation failed: {e}')

        except (OSError, NotImplementedError) as e:
            raise ExceptionID(f'ID generation failed, system error during operation: {e}')

        except Exception as e:
            raise ExceptionID(f'ID generation unexpected error: {e}')

    @classmethod
    def convert(cls, uid_number: UUID) -> str:

        try:
            return str(uid_number)

        except Exception as e:
            raise ExceptionID(f'ID converting (from UUID to string) unexpected error: {e}')

    @classmethod
    def validate(cls, uid_number: UUID | str) -> bool:

        from config import REGEX_UID4, REGEX_UID5

        try:
            if isinstance(uid_number, str):
                uid_number: str = str(uid_number)

            elif not isinstance(uid_number, UUID):
                raise ExceptionID('ID processing failed, data type error during verification')

            if REGEX_UID4.fullmatch(string=uid_number) or REGEX_UID5.fullmatch(string=uid_number):
                return True

            return False

        except Exception as e:
            raise ExceptionID(f'ID processing failed, verification error: {e}')


if __name__ == '__main__':
    ProcessorID.__i
