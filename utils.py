from typing import Callable, Tuple, List
import inspect
import numpy as np
import matplotlib.pyplot as plt


Func = Callable[[float], float]
Interval = Tuple[float, float]

"""The first Func in each tuple is g(x) and the second Func is the 1st derivative of g(x)"""
GXs = List[Tuple[Func, Func]]


kMaxNumIterations: int = 100
kFloatingJitter = 10e-9


def findInterval(f: Func, step: float = 1.0) -> Interval:
    a, b = 0.0, 1.0
    fa, fb = f(a), f(b)
    while fa*fb > 0:
        if fa*fb == 0:
            raise ValueError("No interval for `f` with step={} contains roots")
        a = b
        fa = fb
        b += step
        fb = f(b)
    return (a, b)


def funcString(f: Func) -> str:
    return ' '.join(inspect.getsource(f).split('=')[1].split(' ')[3:]).strip()


def printSummary(question: str, f: Func, interval: Interval, roots: List[Tuple[float, float]]):
    numIterations = len(roots)
    numIterations_ = str(numIterations)
    if (numIterations == kMaxNumIterations):
        numIterations_ = "{} (max)".format(numIterations)
    question = "Question: {}".format(question)
    print("{}\n{}".format(question, '-' * len(question)))
    print("f(x) = {}\nInterval = {}\nNum iterations = {}".format(funcString(f), interval, numIterations_))
    print("Root = {}\n\n".format(roots[-1]))


def plotFunc(f: Func):
    x = np.linspace(0.1, 4, 50)
    plt.plot(x, f(x))   # type:ignore
    plt.show(block=False)
    plt.waitforbuttonpress()
    plt.close()
