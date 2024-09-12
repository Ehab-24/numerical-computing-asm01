from utils import Func, Interval # type:ignore
from typing import List


def findRootNewtonRalphson(f: Func, f_: Func, interval: Interval, threshold: float = 10e-2) -> List[float]:
    xs: List[float] = []

    def error(xs: List[float]) -> float:
        return abs(xs[-1] - xs[-2])

    x1 = (interval[0] + interval[1]) / 2
    xs.append(x1)

    while xs[-1] < interval[1]:
        xs.append(x1 - (f(x1) / f_(x1)))
        if error(xs) < threshold:
            break

    return xs
