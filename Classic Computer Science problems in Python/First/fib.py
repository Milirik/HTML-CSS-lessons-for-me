# -*- coding: utf-8 -*-
from typing import Dict, Generator
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}

def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 1) + fib4(n - 2)

def fib5(n: int) -> int:
    if n==0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

if __name__ == '__main__':
    print(fib5(6))
    print(fib5(50))
    for i in fib6(2):
        print(i)