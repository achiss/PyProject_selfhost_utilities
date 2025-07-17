from pathlib import Path
from typing import Tuple, Any
from tomllib import load

BASE_PATH: Path = Path(__file__).resolve().parent.parent

def get_setting_path() -> Path: return BASE_PATH / 'settings.toml'


class Initializer:
    @classmethod
    def get_settings(cls) -> Tuple[bool, Any]:
        path: Path = get_setting_path()
        if not path.exists(follow_symlinks=False):
            return False, f'configuration file is not exist'

        try:
            with open(path, 'rb') as file:
                config = load(file)

            return True, config

        except Exception as e:
            return False, f'unexpected error while reading configuration file - {e}'


if __name__ == '__main__':
    print(Initializer.get_settings())
