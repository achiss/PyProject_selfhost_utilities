from uuid import UUID
from typing import Any

from src.interface import ProcessorIDProtocol

from src.app_model.process_id.share.convert_id import convert_id
from src.app_model.process_id.share.generate_id import generate_id
from src.app_model.process_id.share.validate_id import validate_id
from src.app_model.process_id.share.validate_method import ValidateMethod

from src.validator import Validator, ValidatorID
from src.core_model import ExceptionID


class ProcessorID(ProcessorIDProtocol):
    @staticmethod
    def convert(uuid_value: UUID | str) -> UUID | str:
        """
        Method: converse ID number data type (UUID <-> str)

        Args:
            uuid_value (UUID or str): value which needs to be converted

        Returns:
            - converting ID data type (if received "UUID" return "str"; if received "str" return "UUID")

        Raises:
            ExceptionID: custom exception, include data:
                - original exception type
                - exception message
                - exception timestamp
        """

        _base_message: str = "Converting ID failed"

        _flag, _result, _type = Validator.check_data_type(UUID, str, checked_value=uuid_value)
        if not _flag:
            _message: str = f'{_base_message}: error in during attribute verification - {_result}'
            raise ExceptionID(original_type=_type, message=_message)

        _flag, _result, _type = convert_id(uuid_value)
        if not _flag:
            _message: str = f'{_base_message}: error in during operation execution - {_result}'
            raise ExceptionID(original_type=_type, message=_message)

        return _result

    @staticmethod
    def generate(*object_data: Any, domain: UUID | None = None) -> UUID: pass

    @staticmethod
    def validate(uuid_value: UUID | str, validate_method: 'ValidateMethod') -> UUID | str: pass


if __name__ == '__main__':
    _id = '5b0d19f5-d911-5042-a651-6ab743d5eb9c'
