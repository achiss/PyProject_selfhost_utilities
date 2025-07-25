from uuid import UUID

from src.interface import IProcessorID


class ProcessorID(IProcessorID):
    @staticmethod
    def convert(value: str | UUID) -> str | UUID: pass

    @staticmethod
    def generate(*object_data: str, domain: UUID) -> UUID: pass

    @staticmethod
    def validate(value: str | UUID) -> bool: pass


if __name__ == '__main__':
    pass
