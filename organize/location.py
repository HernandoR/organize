from enum import Enum
from typing import List, Set, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator
from pydantic.dataclasses import dataclass
from typing_extensions import Literal

DEFAULT_SYSTEM_EXCLUDE_FILES = [
    "thumbs.db",
    "desktop.ini",
    "~$*",
    ".DS_Store",
    ".localized",
]

DEFAULT_SYSTEM_EXCLUDE_DIRS = [
    ".git",
    ".svn",
]


@dataclass(config=ConfigDict(extra="forbid"))
class Location(BaseModel):
    path: str
    max_depth: Union[Literal["inherit"], int, None] = "inherit"
    search: Literal["depth", "breadth"] = "breadth"
    exclude_files: List[str] = Field(default_factory=list)
    exclude_dirs: List[str] = Field(default_factory=list)
    system_exclude_files: List[str] = Field(
        default_factory=lambda: DEFAULT_SYSTEM_EXCLUDE_FILES
    )
    system_exclude_dirs: List[str] = Field(
        default_factory=lambda: DEFAULT_SYSTEM_EXCLUDE_DIRS
    )
    filter: Union[List[str], None] = None
    filter_dirs: Union[List[str], None] = None
    ignore_errors: bool = False

    @field_validator(
        "exclude_files",
        "exclude_dirs",
        "system_exclude_files",
        "system_exclude_dirs",
        mode="before",
    )
    def ensure_list(cls, value):
        if isinstance(value, str):
            return [value]
        return value
