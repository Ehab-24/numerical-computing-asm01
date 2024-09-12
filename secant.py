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
