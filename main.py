from utils import Func, GXs, Interval, printSummary, plotFunc, funcString # type:ignore
from bisection import findRootBisection # type:ignore
from fixed_point_iteration import findRootFixedPointItertion # type:ignore
from newton_ralphson import findRootNewtonRalphson # type:ignore

from numpy import cos, sin, exp, log, sqrt
import warnings


def main():
    ############################################
    # Part (i) - (a)
    ###########################################

    f: Func = lambda x: x**2 - 4*x + log(x)
    interval: Interval = (1, 2)
    roots = findRootBisection(f, interval)

    printSummary("1 (a)", f, interval, roots)

    ############################################
    # Part (i) - (b)
    ###########################################

    f: Func = lambda x: x**2 - 4*x + log(x)
    interval: Interval = (3, 4)
    roots = findRootBisection(f, interval)

    printSummary("1 (b)", f, interval, roots)

    ############################################
    # Part (ii)
    ###########################################

    f: Func = lambda x: cos(exp(x) - 2) - exp(x) + 2
    interval: Interval = (0.5, 1.5)
    roots = findRootBisection(f, interval)

    printSummary("2", f, interval, roots)

    ############################################
    # Part (iii)
    ###########################################

    f: Func = lambda x: x**4 - 3*(x**2) - 3
    gxs: GXs = [
        (
            lambda x: (3*(x**2) + 3)**(1/4),
            lambda x: (1/4) * ((3*(x**2) + 3)**(-3/4)) * 6*x
        ),
        (
            lambda x: (3/(x**2 + 3)) ** (1/2),
            lambda x: ((sqrt(3) * x)) / ((x**2 - 3) ** (3/2))
        ),
        (
            lambda x: sqrt((x**4 - 3) / 3),
            lambda x: (3 * x**3) / (sqrt(3 * (x**4 - 3)))
        ),
        (
            lambda x: sqrt(3 + (3 * x**2)) / x,
            lambda x: (2 / sqrt(1 + x**2)) - (sqrt(1 + x**2) / x**2)
        ),
    ]
    roots = findRootFixedPointItertion(f, 1.0, gxs, (1, 2), threshold=10e-3)
    printSummary("3 (a)", f, interval, roots)

    ############################################
    # Part (iii)
    ###########################################

    f: Func = lambda x: exp(x) + 2**(-x) + 2*cos(x) - 6
    f_: Func = lambda x: exp(x) - 2**(-2*x) - 2*sin(x)
    interval = (1, 2)

    roots = findRootNewtonRalphson(f, f_, interval, threshold=10e-5)
    printSummary("4 (a)", f, interval, roots)


if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        main()
