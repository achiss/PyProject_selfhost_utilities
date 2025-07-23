from uuid import UUID

from src.app_model.process_id.share.convert_id import convert_id
#from src.app_model.process_id.share.generate_id import
#from src.app_model.process_id.share.validate_id import


class ProcessID:
    @staticmethod
    def convert(uuid_value: UUID | str) -> UUID | str: pass

    @staticmethod
    def generate(*object_data, domain: UUID | None = None) -> UUID: pass

    @staticmethod
    def validate(uuid_value: UUID | str) -> UUID | str: pass
