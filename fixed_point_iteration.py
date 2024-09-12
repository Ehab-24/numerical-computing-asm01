from typing import List, Tuple
from utils import Func, Interval, kFloatingJitter, GXs, change, kMaxNumIterations


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
    g_s: List[Tuple[float, Func]] = []
    for g, g_ in gxs:
        try:
            g_x0 = abs(g_(x0))
            g_s.append((g_x0, g))
        except:
            pass

    min_g_ = 2 ** 31 - 1
    min_g = lambda x: x
    for g_x, g in g_s:
        if g_x < min_g_ and g_x > 0+kFloatingJitter:
            min_g_ = g_x
            min_g = g
    if min_g_ >= 1:
        raise ValueError("The given function will not converge")
    return min_g


def findRootFixedPointItertion(x0: float, gxs: GXs, interval: Interval, threshold: float = 10e-3) -> List[float]:
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

    if x0 < interval[0]:
        raise ValueError("`x0` must be inside interval\tx0: {}, Interval: {}".format(x0, interval))
    gx = findGx_(x0, gxs)

    xs: List[float] = [x0]
    n_iterations = 0
    while xs[-1] < interval[1] and n_iterations < kMaxNumIterations:
        n_iterations+=1
        xs.append(gx(xs[-1]))
        if change(xs) < threshold:
            break

    return xs
