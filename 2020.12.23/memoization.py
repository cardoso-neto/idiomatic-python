from urllib import error, request
from functools import lru_cache


@lru_cache(maxsize=32)
def get_pep(num):
    """Retrieve text of a Python Enhancement Proposal."""
    resource = f'http://www.python.org/dev/peps/pep-{num:04}/'
    try:
        with request.urlopen(resource) as s:
            return s.read()
    except error.HTTPError:
        return 'Not Found'


if __name__ == "__main__":
    for n in 8, 290, 308, 320, 218, 279, 289, 320, 9991, 8, 8, 290, 320, 320, 320:
        pep = get_pep(n)
        print(f"PEP {n} has {len(pep)} lines.")
        # PEP 8 has 107687 lines.
        # PEP 290 has 60448 lines.
        # PEP 308 has 57654 lines.
        # ...

    print(get_pep.cache_info())
    # CacheInfo(hits=7, misses=8, maxsize=32, currsize=8)
