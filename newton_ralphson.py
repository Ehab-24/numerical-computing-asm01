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
