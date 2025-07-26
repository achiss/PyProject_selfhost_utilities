from uuid import UUID

from src.interface import IProcessorID

from src.app_model.processor_id.share.convert_id import convert_id
from src.app_model.processor_id.share.generate_id import generate_id
from src.app_model.processor_id.share.validate_id import validate_id

from src.core_model import ExceptionID


class ProcessorID(IProcessorID):
    @staticmethod
    def convert(value: str | UUID) -> str | UUID:
        """
        Method: convert ID value (UUID <-> str)
        
        Args:
            value (str | UUID): converting ID value (from UUID to str | from str to UUID)
        
        Returns:
            str | UUID: converted ID value
        
        Raises:
            ExceptionID (ID processing exception)
        """
        
        _flag, _result, _type = convert_id(value)
        if not _flag:
            _message: str = f'Converted ID error, {_result}.'
            raise ExceptionID(original_exception = _type, exception_message = _message)

        return _result

    @staticmethod
    def generate(*object_data: str, domain: UUID) -> UUID: pass

    @staticmethod
    def validate(value: str | UUID) -> bool: pass


if __name__ == '__main__':
    print(ProcessorID.convert('invalid'))
