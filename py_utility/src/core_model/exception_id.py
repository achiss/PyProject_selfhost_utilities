from typing import Type, Any

from src.core_model.base_model import BaseExceptionModel


class ExceptionID(BaseExceptionModel):
    def __init__(self, original_type: Type[Any] | None, message: str) -> None:
        super().__init__(
            custom_type=ExceptionID,
            original_type=original_type,
            message=message,
        )
