from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print([fib(n) for n in range(16)])
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    print(fib.cache_info())
    # CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)
