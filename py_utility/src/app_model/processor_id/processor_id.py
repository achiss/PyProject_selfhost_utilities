from uuid import UUID

from src.interface import IProcessorID

from src.app_model.processor_id.share.core.verification_convert_data import verification_convert_data
from src.app_model.processor_id.share.core.convert_data import convert_data

from src.core_model import ExceptionID


class ProcessorID(IProcessorID):
    @staticmethod
    def convert(value: str | UUID) -> str | UUID:
        
        if not (_result := verification_convert_data(value))[0]:
            _message: str = f'Converted ID error, {_result[1]}.'
            raise ExceptionID(original_exception_type = _result[2], exception_message = _message)

        _flag, _result, _type = convert_data(value)
        if not _flag:
            _message: str = f'Converted ID error, {_result}.'
            raise ExceptionID(original_exception_type = _type, exception_message = _message)
        
        return _result

    @staticmethod
    def generate(*object_data: str, domain: UUID) -> UUID: pass

    @staticmethod
    def validate(value: str | UUID) -> bool: pass


if __name__ == '__main__':
    print(ProcessorID.convert('invalid'))
