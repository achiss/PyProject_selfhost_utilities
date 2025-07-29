from datetime import datetime


def get_datetime() -> str:

    from data.format import DATETIME_ISO

    return datetime.now().strftime(format = DATETIME_ISO)
