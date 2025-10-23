# pylint: disable=missing-module-docstring
def trois_d_printer(x):
    """
    Calculate the minimum number of days required for a printer to produce
    at least `x` copies, given the following rules:
    
    - On day 1, there is 1 printer available.
    - Each subsequent day, every existing printer produces one copy.
    - At the end of each day, you can build additional printers equal to
      the number of copies produced that day.
    - Effectively, the number of printers grows by powers of 2 each day.
    
    Parameters
    ----------
    x : int
        The target number of copies to produce.
    
    Returns
    -------
    int
        The minimum number of days required to produce at least `x` copies.
    
    Examples
    --------
    >>> main(1)
    1
    >>> main(5)
    3
    >>> main(20)
    5
    """
    printer = 1
    day = 0
    while printer < x :
        printer = printer + 2**day
        day+=1
    return day+1
