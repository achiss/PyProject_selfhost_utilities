from uuid import UUID

from src.share.processor_id.interface import IProcessorID
from src.share.processor_id.core.generation_uid import GenerationUid
from src.share.processor_id.core.verification_uid import VerificationUid

from src.validator import ValidatorCommon
from src.core import ExceptionID


class ProcessorID(IProcessorID):
    @classmethod
    def generate(cls, domain: UUID = None, *args: str) -> UUID:
        """
        Method: generation ID number

        Args:
            domain (UUID): UUID number as namespace (for UUID version 5)
            *args (str): object string as name (for UUID version 5)

        Returns:
            - (UUID): id number
            (if without arguments generating by uuid4, otherwise by uuid5)

        Raises:
            ExceptionID: custom exception class for ProcessorID class
        """

        try:
            if len(args) == 0 and isinstance(domain, UUID):
                raise AttributeError('parameter (object data) is required when parameter (domain) is provided')

            elif len(args) != 0 and not isinstance(domain, UUID):
                raise AttributeError('parameter (domain) is required when parameter (object data) is provided')

            object_data: str = ''
            if len(args) != 0:
                for arg in args:
                    object_data += arg

            flag, action = GenerationUid.generate(domain=domain, object_data=object_data)
            if not flag:
                raise RuntimeError(action)

            return action

        except (AttributeError, RuntimeError) as e:
            message: str = 'ID processing > generation function'
            raise ExceptionID(f'{message} - {e}')

        except Exception as e:
            message: str = 'ID processing > unexpected error during generation function'
            raise ExceptionID(f'{message} - {e}')


    @classmethod
    def validate(cls, uid_number: str | UUID) -> bool:
        """
        Method: verification ID number

        Args:
            uid_number (UUID): verifying ID number

        Returns:
            - True if success, otherwise False

        Raises:
            ExceptionID: custom exception class for ProcessorID class
        """

        try:
            if not (action := ValidatorCommon.check_data_type(str, UUID, checked_value=uid_number))[0]:
                raise TypeError(action[1])

            flag, action = VerificationUid.validate(uid_number)
            if not flag and action:
                raise RuntimeError(action)

            elif not (flag and action):
                return False

            return True

        except (TypeError, RuntimeError) as e:
            message: str = 'ID processing > verifying function'
            raise ExceptionID(f'{message} - {e}')

        except Exception as e:
            message: str = 'ID processing > unexpected error during verifying function'
            raise ExceptionID(f'{message} - {e}')

    @classmethod
    def convert(cls, uid_number: UUID) -> str:
        """
        Method: converted UUID to string

        Args:
            uid_number (UUID): id number for conversion

        Returns:
            - (string): id number

        Raises:
            ExceptionID: custom exception class for ProcessorID class
        """

        try:
            if not (action := ValidatorCommon.check_data_type(UUID, checked_value=uid_number))[0]:
                raise TypeError(action[1])

            return str(uid_number)

        except TypeError as e:
            message: str = 'ID processing > converting function'
            raise ExceptionID(f'{message} - {e}')

        except Exception as e:
            message: str = 'ID processing > unexpected error during converting function'
            raise ExceptionID(f'{message} - {e}')


if __name__ == '__main__':
    uid = ProcessorID()
    print(uid.generate())
