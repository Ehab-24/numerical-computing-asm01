from utils import Func, Interval, kMaxNumIterations
from typing import List


def findRootBisection(f: Func, interval: Interval, roots: List[float] = [], threshold: float = 10e-6, recursionCount: int = 0) -> List[float]:
    recursionCount += 1

    if recursionCount > kMaxNumIterations:
        return []

    a, b = interval
    x = (a + b) / 2
    fx = f(x)
    if abs(fx) < threshold:
        return [x]

    if fx * f(a) > 0:
        a = x
    else:
        b = x
    return [x] + findRootBisection(f, (a, b), roots + [x], threshold, recursionCount)
