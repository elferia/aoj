from bisect import bisect_left, bisect_right
from collections import deque
from functools import partial
from itertools import islice
from math import sqrt
from operator import itemgetter, methodcaller
from sys import stdin

consume = deque(maxlen=0).extend

point_count = int(input())
points = [
    (*it, i) for i, it in
    enumerate(
        map(partial(map, int),
            map(methodcaller('split'), islice(stdin, point_count))))]
points.sort()

x_node_interval = int(sqrt(point_count))
lower_bounds = [p[0] for p in points[::x_node_interval]]
upper_bounds = [p[0] for p in points[x_node_interval - 1::x_node_interval]]
upper_bounds.append(1_000_000_000 + 1)
x_ascending_groups = [
    points[i:i + x_node_interval] for i in
    range(0, point_count, x_node_interval)]
consume(map(methodcaller('sort', key=itemgetter(1)), x_ascending_groups))
x_ascending_groups = [
    ([p[1] for p in group], group) for group in x_ascending_groups]

query_count = int(input())
for sx, tx, sy, ty in map(
    tuple,
        map(partial(map, int),
            map(methodcaller('split'), islice(stdin, query_count)))):
    answer = []
    group_start = bisect_left(upper_bounds, sx)
    for group_index in range(
            group_start, bisect_right(lower_bounds, tx, lo=group_start)):
        ys, members = x_ascending_groups[group_index]
        member_start = bisect_left(ys, sy)
        for member_index in range(
                member_start, bisect_right(ys, ty, lo=member_start)):
            if sx <= members[member_index][0] <= tx:
                answer.append(members[member_index][2])
    if answer:
        answer.sort()
        print('\n'.join(map(str, answer)))
    print()
