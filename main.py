#!/usr/bin/uv run

# pyright: reportUnknownMemberType=false, reportUnknownVariableType=false, reportMissingImports=false

from sympy import isprime
import matplotlib.pyplot as plt

SEARCH_MAX = 1000


def check(n: int) -> bool:
    return isprime(n) and isprime(n + 2)


def main():
    print(f'Searching for twin primes under {SEARCH_MAX}')
    found = [i for i in range(SEARCH_MAX) if check(i)]
    print(f'Found twin primes: {found}')
    plt.hist(found, bins=10)
    plt.title('Distrubution of Twin Primes')
    plt.xlabel('The smaller twin')
    plt.ylabel('Count')
    plt.show()


if __name__ == '__main__':
    main()
