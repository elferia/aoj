from bisect import bisect_left
from itertools import islice
from sys import stdin

array_len = int(input())
array = map(int, islice(stdin, array_len))

values = []
incre_s_lens = []


def update(value: int) -> None:
    pos = bisect_left(values, value)

    if pos == len(values):
        incre_s_len = (incre_s_lens[pos - 1] if pos else 0) + 1
        values.append(value)
        incre_s_lens.append(incre_s_len)
    elif value < values[pos]:
        values[pos] = value


for i in array:
    update(i)

print(incre_s_lens[-1])
