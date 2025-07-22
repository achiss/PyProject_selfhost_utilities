from typing import Tuple, List


def check_arg_object_string(*args: str) -> Tuple[bool, str]:

    if len(args) == 0:
        return False, f'parameter (object string), cannot be empty'

    else:
        data: List[str] = []
        for i, item in enumerate(args):
            if isinstance(item, str):
                data.append(item)

            elif isinstance(item, bytes):
                item: str = str(item)
                data.append(item)

            else:
                return False, f'parameter (object string) at position ({i}), cannot be converted to bytes'

        return True, ' '.join(data)
