from src.utility import ProcessorID
from src.utility.id.proxy_id import ProxyID


class Utility:
    __slots__ = ('_id',)

    def __init__(self):
        self._id = ProcessorID()

    @property
    def id(self) -> 'ProxyID': return ProxyID(self._id)


if __name__ == '__main__':
    utility = Utility()
    utility.id.