def fibonacci(n):
    """
    Returns nth Fibonacci Number
    Series starting with the integers 0 and 1
    [0, 1, 1, 2, 3, 5, 8, 13, ...]
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """
    Returns nth Lucas Number
    Series starting with the integers 2 and 1
    [2, 1, 3, 4, 7, 11, 18, 29, ...]
    """

    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

def sum_series(n, first = 0, second = 1):
    """
    The first parameter will determine which element in the series to print
    The second and third parameter will have a default of 0 and 1 and will determine the first two values of the series
    """

    if n == 0:
        return first
    elif n == 1:
        return second
    return sum_series(n-1, first, second) + sum_series(n-2, first, second)
