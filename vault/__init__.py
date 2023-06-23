import os
from typing import Optional

from .main import _variables


def from_env_or_vault(env_name: str, default: Optional[str] = None) -> Optional[str]:
    return os.environ.get(env_name, _variables.get(env_name, default))


def from_vault(key: str) -> Optional[str]:
    return _variables[key]
