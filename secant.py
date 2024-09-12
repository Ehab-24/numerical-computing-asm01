from utils import Func, Interval, change, kMaxNumIterations
from typing import List


def secant_(f: Func, x1: float, x2: float) -> float:
    return (x1*f(x2) - x2*f(x1)) / (f(x2) - f(x1))


def findRootSecant(f: Func, interval: Interval, threshold: float = 10e-6) -> List[float]:

    x0, x1 = interval
    xs: List[float] = [x0, x1]

    n_iterations = 0
    while n_iterations < kMaxNumIterations:
        n_iterations+=1
        xs.append(secant_(f, xs[-2], xs[-1]))
        if change(xs) < threshold:
            return xs

    return xs
