from uuid import UUID
from datetime import datetime

from src.share import IProcessorID
from src.share import generate_id

from src.core import ExceptionID


def get_timestamp() -> str: return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class ProcessorID(IProcessorID):
    @staticmethod
    def generate(*object_string: str | None, domain: UUID | None = None) -> UUID:
        try:
            if len(object_string) == 0 and domain:
                raise AttributeError(f'Processor ID, attribute error')

            elif len(object_string) != 0 and not domain:
                raise AttributeError(f'Processor ID, attribute error')

            _string: str = ''
            if len(object_string) != 0:
                for arg in object_string:
                    _string += str(arg)

            else:
                _string: None = None

            flag, result = generate_id(object_string=_string, domain=domain)
            if not flag:
                raise RuntimeError(result)

            return result

        except RuntimeError as e:
            raise ExceptionID(f'{e}', RuntimeError, get_timestamp())

        except Exception as e:
            message: str = 'Processor ID, unexpected error'
            raise ExceptionID(f'{message} - {e}', Exception, get_timestamp())

    @staticmethod
    def validate(uuid_number: str | UUID) -> bool: pass

    @staticmethod
    def convert(uuid_number: str | UUID) -> str: pass


if __name__ == '__main__':
    pass
