from pathlib import Path

SERVICE_DIR = Path(__file__).resolve().parent.parent

BASE_DIR = SERVICE_DIR.parent

CONFIGURATION_PATH = f'{SERVICE_DIR}/configuration.json'

DB_PATH = f'{BASE_DIR}/db.sqlite3'

__all__ = [
    'SERVICE_DIR',
    'BASE_DIR',
    'CONFIGURATION_PATH',
    'DB_PATH',
]
