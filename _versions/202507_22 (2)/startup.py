from pathlib import Path


# BASE DIR
BASE_DIR: Path = Path(__file__).resolve().parent


# DATA DIR
DATA_DIR: Path = BASE_DIR / 'data'


# SETTINGS PATH
SETTINGS_ID_PATH: Path = BASE_DIR / 'config/settings_id.toml'

SETTINGS_IO_PATH: Path = BASE_DIR / 'config/settings_io.toml'

SETTINGS_SECRET_PATH: Path = BASE_DIR / 'config/settings_secret.toml'
