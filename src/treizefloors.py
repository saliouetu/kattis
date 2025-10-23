# pylint: disable=missing-module-docstring
def treize_floors(x):
    """
    Adjust floor numbering to skip the 13th floor, as is common in some
    buildings.

    - If the floor number is between 0 and 12 (inclusive), return it unchanged.
    - If the floor number is 13 or higher, shift it up by 1 to skip floor 13.

    Parameters
    ----------
    x : int
        The floor number in a "natural" sequence (without skipping 13).

    Returns
    -------
    int
        The adjusted floor number, skipping 13.

    Examples
    --------
    >>> treize_floors(0)
    0
    >>> treize_floors(12)
    12
    >>> treize_floors(13)
    14
    >>> treize_floors(20)
    21
    """
    if x in range(0,13):
        return x
    return x+1
