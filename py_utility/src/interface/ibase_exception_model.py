from abc import ABC, abstractmethod
from typing import Type


class IBaseExceptionModel(Exception, ABC):
	pass
