from functools import partial
from itertools import islice
from operator import methodcaller
from sys import stdin

item_count, max_weight = [int(s) for s in input().split()]
items = [
    (*it,) for it in
    map(partial(map, int),
        map(methodcaller('split'), islice(stdin, item_count)))]

values = [0]
values.extend(-1 for _ in range(max_weight))

for item_index in range(item_count):
    item_weight = items[item_index][1]
    _values = values[:item_weight]
    for current_weight in range(item_weight, max_weight + 1):
        light_value = values[current_weight - item_weight]
        _values.append(
            max((-1 if light_value == -1 else
                 light_value + items[item_index][0]), values[current_weight]))
    values = _values

print(max(values))
