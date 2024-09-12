"""
Copyright [2024] Ehab Sohail

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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


def printSummary(question: str, f: Func, interval: Interval, roots: List[float]):
    numIterations = len(roots)
    numIterations_ = str(numIterations)
    if (numIterations == kMaxNumIterations):
        numIterations_ = "{}\t(MAX LIMIT)".format(numIterations)
    question = "Question: {}".format(question)
    print("{}\n{}".format(question, '-' * len(question)))
    print("f(x) = {}\nInterval = {}\nNum iterations = {}".format(funcString(f), interval, numIterations_))
    print("Root = {}\n\n".format(roots[-1]))


def plotFunc(f: Func, root: float, interval: Interval):
    """
    Plots the function `f` and optionally displays a specific point on the graph.

    Parameters:
    - f (Func): The function to plot.
    - root (float): The root of `f`
    """
    a, b = interval
    x = np.linspace(a, b, 50)
    plt.plot(x, f(x), label="f(x) = {}".format(funcString(f)))   # type:ignore
    
    f_root = f(root)
    plt.scatter(root, f_root, color='red', zorder=5, label="f({}) = {}".format(root, f_root))
    
    plt.legend()
    plt.show(block=False)
    plt.waitforbuttonpress()
    plt.close()


def change(xs: List[float]) -> float:
    return abs(xs[-1] - xs[-2])
