"""Flag enumeration module for NASCAR API.

This module defines the Flag enum representing different flag states
used in NASCAR races.
"""

from enum import IntEnum


class Flag(IntEnum):
    """NASCAR flag states used during races.

    Represents the different types of flags that can be displayed
    during a NASCAR race to communicate race conditions to drivers.
    """

    GREEN = 1
    YELLOW = 2
    RED = 3
    WHITE = 4
    CHECKERED = 5
    HOT_TRACK = 8
    COLD_TRACK = 9
