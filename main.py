#!/usr/bin/uv run

# pyright: reportUnknownMemberType=false, reportUnknownVariableType=false, reportMissingImports=false, reportMissingTypeStubs=false

from sympy import isprime
import matplotlib.pyplot as plt
from scipy.integrate import quad
from math import log

SEARCH_MAX = 1000
INTERVAL_CNT = 10

bin_size = SEARCH_MAX / INTERVAL_CNT


def check(n: int) -> bool:
    return isprime(n) and isprime(n + 2)


def hardy_littlewood(lower: float, upper: float) -> float:
    C2 = 1.320323632

    def f(x: float):
        return 1 / log(x) ** 2

    i, _err = quad(f, lower, upper)

    return C2 * i


def main():
    print(f'Searching for twin primes under {SEARCH_MAX}')
    found = [i for i in range(SEARCH_MAX) if check(i)]
    print(f'Found {len(found)} twin prime pairs.')

    def plot_hist():
        _ = plt.hist(found, bins=INTERVAL_CNT)
        _ = plt.title('Distrubution of Twin Primes')
        _ = plt.xlabel('The smaller twin')
        _ = plt.ylabel('Count')

    plot_hist()

    def plot_estimate():
        plot_hist()

        x = [i * bin_size for i in range(INTERVAL_CNT)]

        def f(n: float) -> float:
            return hardy_littlewood(max(2, n), n + bin_size)

        y = [f(i) for i in x]

        _ = plt.plot(x, y)

    plot_estimate()

    plt.show()


if __name__ == '__main__':
    main()
