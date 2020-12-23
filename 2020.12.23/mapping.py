import itertools
from operator import methodcaller


names = ["matheus", "nelson"]

capitalized_names = [x.upper() for x in names]
capitalized_names = map(lambda x: x.upper(), names)
capitalized_names = map(methodcaller("upper"), names)

print(capitalized_names)
# <map object at 0xffffffffffff>

# map returns an iterator and only when you consume the iterator that the
# computation will actually run.
# That's what it means to be lazy. It delays computations untill they're needed.
# And it only does one iteration at a time, keeping memory usage low.

print(*capitalized_names)
# MATHEUS NELSON
print([name for name in capitalized_names])
# []

# When an iterator is consumed or exhausted, you can't reconsume it as it will
# not "yield" anymore.

numbers = iter([1, 2])
next(numbers)  # number.__next__()
# 1
next(numbers)
# 2
next(numbers)
# StopIteration

# Whet if you need to use the same iterator several times?
# You can create a list with it and the use that list as many times as necessary
numbers_list = list(iter([1, 2]))
# But that loads everything into RAM, if you can't do that, use tee to create
# as as many as needed
iterator_1, iterator_2 = itertools.tee(numbers, 2)
