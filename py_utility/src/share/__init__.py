# Section: COMMON
from src.share.base_validator_data_type import check_data_type
from src.share.base_validator_length import check_length
from src.share.base_model_messaeger import (TYPE_ERROR_TEMPLATE, EMPTY_LIST_ERROR_TEMPLATE, ATTRIBUTE_ERROR_TEMPLATE,
                                            UNEXPECTED_ERROR_TEMPLATE)

# Section: ID PROCESSING
from src.share.model_id_regex import REGEX_UUID, REGEX_UUID4, REGEX_UUID5
