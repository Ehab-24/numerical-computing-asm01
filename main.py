from utils import Func, GXs, Interval, printSummary, plotFunc
from bisection import findRootBisection
from fixed_point_iteration import findRootFixedPointItertion
from newton_ralphson import findRootNewtonRalphson
from secant import findRootSecant

from numpy import cos, sin, exp, log, sqrt
import warnings


def main():

    ############################################
    # Question 1 (a)
    ###########################################

    f: Func = lambda x: x**2 - 4*x + log(x)
    interval: Interval = (1, 2)
    roots = findRootBisection(f, interval)

    printSummary("1 (a)", f, interval, roots)
    plotFunc(f, roots[-1], interval)

    ############################################
    # Question 1 (b)
    ###########################################

    f: Func = lambda x: x**2 - 4*x + log(x)
    interval: Interval = (2, 4)
    roots = findRootBisection(f, interval)

    printSummary("1 (b)", f, interval, roots)
    plotFunc(f, roots[-1], interval)

    ############################################
    # Question 2
    ###########################################

    f: Func = lambda x: cos(exp(x) - 2) - exp(x) + 2
    interval: Interval = (0.5, 1.5)
    roots = findRootBisection(f, interval)

    printSummary("2", f, interval, roots)
    plotFunc(f, roots[-1], interval)

    ############################################
    # Question 3 (a)
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
    roots = findRootFixedPointItertion(1.0, gxs, (1, 2))
    printSummary("3 (a)", f, interval, roots)

    ############################################
    # Question 3 (b)
    ###########################################

    f: Func = lambda x: x**3 - x - 1
    gxs: GXs = [
        (
            lambda x: x**3 - 1,
            lambda x: 3 * x**2
        ),
        (
            lambda x: 1 / (x**2 - 1),
            lambda x: (-2*x) / (x**2 - 1)**2
        ),
        (
            lambda x: (x + 1) ** (1/3),
            lambda x: (1/3) / (x + 1)**(2/3)
        ),
        (
            lambda x: (1/x) + (1/x**2),
            lambda x: (-1/x**2) - (2/x**3)
        ),
        (
            lambda x: sqrt((x + 1) / x),
            lambda x: -1 / (2 * sqrt(x * (x + 1)))
        )
    ]
    roots = findRootFixedPointItertion(1.0, gxs, (1, 2))
    printSummary("3 (b)", f, interval, roots)
    plotFunc(f, roots[-1], interval)

    ############################################
    # Question 4 (a)
    ###########################################

    f: Func = lambda x: exp(x) + 2**(-x) + 2*cos(x) - 6
    f_: Func = lambda x: exp(x) - 2**(-2*x) - 2*sin(x)
    interval = (1, 2)

    roots = findRootNewtonRalphson(f, f_, interval)
    printSummary("4 (a)", f, interval, roots)

    ############################################
    # Question 4 (b)
    ###########################################
    
    f: Func = lambda x: log(x-1) + cos(x-1)
    interval = (1.3, 2)

    roots = findRootSecant(f, interval)
    printSummary("4 (b)", f, interval, roots)
    plotFunc(f, roots[-1], interval)

    ############################################
    # Question 5
    ###########################################
    
    f: Func = lambda x: x**2 - 4*x + 4 - log(x)
    f_: Func = lambda x: 2*x - 4 - (1/x)
    interval = (1, 2)

    roots = findRootNewtonRalphson(f, f_, interval)
    printSummary("5 (a) - Newton-Ralphson", f, interval, roots)

    roots = findRootSecant(f, interval)
    printSummary("5 (a) - Secant", f, interval, roots)

    interval = (2, 4)

    roots = findRootNewtonRalphson(f, f_, interval)
    printSummary("5 (b) - Newton-Ralphson", f, interval, roots)

    roots = findRootSecant(f, interval)
    printSummary("5 (b) - Secant", f, interval, roots)

    plotFunc(f, roots[-1], interval)


if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        main()
