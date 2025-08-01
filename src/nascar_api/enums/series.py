"""Series enumeration module for NASCAR API.

This module defines the Series enum representing different NASCAR series.
"""

from enum import IntEnum


class Series(IntEnum):
    """NASCAR series enumeration.

    Represents the different NASCAR racing series that can be accessed
    through the NASCAR API.
    """

    CUP = 1
    XFINITY = 2
    TRUCK = 3



