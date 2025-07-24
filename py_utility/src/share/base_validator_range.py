from typing import overload
from typing import Tuple, Type


@overload



def check_range(checked_value: int | float = None, lower_bound: int | float = None, upper_bound: int | float = None,
                included_lower: bool = False, included_upper: bool = False) \
		-> Tuple[bool, str | None, Type[Exception] | None]: pass
