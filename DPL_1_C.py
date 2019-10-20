from collections import deque
from functools import partial
from itertools import islice
from operator import methodcaller
from sys import stdin
from typing import Tuple

item_count, max_weight = [int(s) for s in input().split()]
items = [
    (*it,) for it in
    map(partial(map, int),
        map(methodcaller('split'), islice(stdin, item_count)))]

values = [0]
values.extend(-1 for _ in range(max_weight))


def update_values(item: Tuple[int, int]) -> None:
    item_weight = item[1]

    for current_weight in range(item_weight, max_weight + 1):
        light_value = values[current_weight - item_weight]
        new_value = -1 if light_value == -1 else light_value + item[0]
        if new_value > values[current_weight]:
            values[current_weight] = new_value


deque(map(update_values, items), maxlen=0)
print(max(values))
