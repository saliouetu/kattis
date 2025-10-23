# pylint: disable=missing-module-docstring
def listgame(n):
    """
    Count the total number of prime factors of a given number `n`.

    The function performs prime factorization by checking divisibility
    starting from 2 and counting all occurrences of each prime factor.
    If `n` is greater than 1 after factoring out smaller primes, it is
    also counted as a prime factor.

    Parameters
    ----------
    n : int
        The integer to factorize (should be >= 1).

    Returns
    -------
    int
        The total count of prime factors of `n`, including multiplicities.

    Examples
    --------
    >>> listgame(18)
    3
    # Explanation: 18 = 2 * 3 * 3, so there are 3 prime factors.
    
    >>> listgame(7)
    1
    # Explanation: 7 is prime, so it has 1 prime factor.

    >>> listgame(60)
    4
    # Explanation: 60 = 2 * 2 * 3 * 5, so 4 prime factors in total.
    """
    count = 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            count += 1
        d += 1
    if n > 1:
        count += 1
    return count 
