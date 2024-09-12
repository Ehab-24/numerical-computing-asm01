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
