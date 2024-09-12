from typing import List
from utils import Func, funcString, Interval, kFloatingJitter, kMaxNumIterations, GXs #type:ignore


def findGx_(x0: float, gxs: GXs) -> Func:
    """Find g(x) that is most suitable for convergence

    Parameters:
    - x0 (float): initial value of x
    - gxs (GXs): A list of tuples, where each tuple contains two functions:
      - g(x): A function that represents the transformation for fixed-point iteration.
      - g_prime(x): The derivative of the g(x) function, used for convergence analysis.

    Returns:
    - Func: g(x) that is most suitable for convergence
    """
    g_s = [(abs(g_(x0)), g) for g, g_ in gxs]

    min_g_ = 2 ** 31 - 1
    min_g = lambda x: x
    for g_x, g in g_s:
        if g_x < min_g_ and g_x > 0+kFloatingJitter:
            min_g_ = g_x
            min_g = g
    if min_g_ >= 1:
        raise ValueError("The given function will not converge")
    return min_g


def findRootFixedPointItertion(f: Func, x0: float, gxs: GXs, interval: Interval, threshold: float = 10e-2) -> List[float]:
    """
    Applies fixed-point iteration to find the root of the given function `f`.

    Parameters:
    - f (Func): The function for which the root is being sought.
    - x0 (float): initial value of x
    - gxs (GXs): A list of tuples, where each tuple contains two functions:
      - g(x): A function that represents the transformation for fixed-point iteration.
      - g_prime(x): The derivative of the g(x) function, used for convergence analysis.

    Returns:
    - float: The approximated root of the function `f` after applying the fixed-point iteration process.
    """

    def error(xs: List[float]) -> float:
        return abs(xs[-1] - xs[-2])

    if x0 < interval[0]:
        raise ValueError("`x0` must be inside interval\tx0: {}, Interval: {}".format(x0, interval))
    gx = findGx_(x0, gxs)

    xs: List[float] = [x0]
    while xs[-1] < interval[1]:
        xs.append(gx(xs[-1]))
        if error(xs) < threshold:
            break

    return xs
