def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """


    x1 = x[:1] + x
    x2 = x + x[-1:]
    xdiff = []
    for i in range(len(x1)):
        xdiff.append(x2[i]-x1[i])

    print(xdiff[1:])

find_maxima([2,2,3,2,3])

