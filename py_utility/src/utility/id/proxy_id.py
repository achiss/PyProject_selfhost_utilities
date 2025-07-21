from uuid import UUID

from src.utility.id.extra.processor_id import ProcessorID


class ProxyID:
    __slots__ = ('__processor_id',)

    def __init__(self, processor_id: 'ProcessorID'):
        self.__processor_id = processor_id

    def generate(self, domain: UUID = None, *object_string: str) -> UUID:
        return self.__processor_id.generate()
