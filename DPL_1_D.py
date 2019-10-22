from bisect import bisect_left
from itertools import islice
from sys import stdin

array_len = int(input())
array = map(int, islice(stdin, array_len))

values = []
incre_s_lens = []


def update(value: int) -> None:
    pos = bisect_left(values, value)
    incre_s_len = max(islice(incre_s_lens, pos), default=0) + 1
    if pos < len(values) and value == values[pos]:
        if incre_s_len > incre_s_lens[pos]:
            incre_s_lens[pos] = incre_s_len
    else:
        values.insert(pos, value)
        incre_s_lens.insert(pos, incre_s_len)


for i in array:
    update(i)

print(max(incre_s_lens))
