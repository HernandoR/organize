from typing import Union

from pydantic import Field
from typing_extensions import Annotated

from .action import Action
from .confirm import Confirm
from .copy import Copy
from .delete import Delete
from .echo import Echo
from .macos_tags import MacOSTags
from .move import Move
from .python import Python
from .rename import Rename
from .shell import Shell
from .symlink import Symlink
from .trash import Trash
from .write import Write

ActionType = Union[
    Action,
    Annotated[
        Union[
            Confirm,
            Copy,
            Delete,
            Echo,
            MacOSTags,
            Move,
            Python,
            Rename,
            Shell,
            Symlink,
            Trash,
            Write,
        ],
        Field(discriminator="name"),
    ],
]
