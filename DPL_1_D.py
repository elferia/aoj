from bisect import bisect_left
from itertools import islice
from sys import stdin

array_len = int(input())
array = map(int, islice(stdin, array_len))

values = []
incre_s_lens = []


def update(value: int) -> None:
    pos = bisect_left(values, value)
    incre_s_len = (incre_s_lens[pos - 1] if pos else 0) + 1

    def remove_elem(i: int) -> None:
        if incre_s_lens[i] == incre_s_len:
            values.pop(i)
            incre_s_lens.pop(i)

    if pos < len(values) and value == values[pos]:
        if incre_s_len > incre_s_lens[pos]:
            incre_s_lens[pos] = incre_s_len
            for i in range(len(incre_s_lens) - 1, pos, -1):
                remove_elem(i)
    else:
        for i in range(len(incre_s_lens) - 1, pos - 1, -1):
            remove_elem(i)

        values.insert(pos, value)
        incre_s_lens.insert(pos, incre_s_len)


for i in array:
    update(i)

print(incre_s_lens[-1])
