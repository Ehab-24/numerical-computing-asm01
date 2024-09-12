from utils import Func, Interval, kMaxNumIterations, change
from typing import List


def findRootNewtonRalphson(f: Func, f_: Func, interval: Interval, threshold: float = 10e-6) -> List[float]:
    xs: List[float] = []

    x1 = (interval[0] + interval[1]) / 2
    xs.append(x1)

    n_iterations = 0
    while xs[-1] < interval[1] and n_iterations < kMaxNumIterations:
        n_iterations += 1
        xs.append(x1 - (f(x1) / f_(x1)))
        if change(xs) < threshold:
            break

    return xs
