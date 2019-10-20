from bisect import bisect_left
from collections import deque
from functools import partial
from itertools import islice
from operator import itemgetter, methodcaller
from sys import stdin
from typing import List, Tuple

point_count = int(input())
point_lines = list(islice(stdin, point_count))

query_count = int(input())

Query = Tuple[Tuple[int, int], Tuple[int, int]]


def solve_query(query: Query) -> None:
    queue = deque((root,))
    answers = []
    while queue:
        node = queue.popleft()
        index, children = node.search(query)
        if index >= 0:
            answers.append(index)
            if len(answers) == 100:
                break
        queue.extend(children)
    if answers:
        answers.sort()
        print('\n'.join(map(str, answers)))
    print()


class Node:
    def __init__(
            self, points: List[Tuple[int, int, int]], axis_index: int = 0
    ) -> None:
        self.axis_index = axis_index
        self.o_axis_index = (axis_index + 1) % 2
        self.points = points
        self.point = None
        self.left = []
        self.right = []

    def search(self, query: Query) -> Tuple[int, List['Node']]:
        if not self.point:
            self._setup()

        p0 = self.point[self.axis_index]
        s0, t0 = query[self.axis_index]

        if t0 < p0:
            return -1, self.left

        p1 = self.point[self.o_axis_index]
        s1, t1 = query[self.o_axis_index]
        if p0 <= s0:
            return (
                self.point[2] if p0 == s0 and s1 <= p1 <= t1 else -1,
                self.right)

        return self.point[2] if s1 <= p1 <= t1 else -1, self.left + self.right

    def _setup(self) -> None:
        self.points.sort(key=itemgetter(self.axis_index))
        axis_values = [p[self.axis_index] for p in self.points]
        median_index = len(self.points) // 2
        median_index = bisect_left(
            axis_values, axis_values[median_index], hi=median_index + 1)
        self.point = self.points[median_index]
        if median_index > 0:
            self.left.append(
                Node(self.points[:median_index], self.o_axis_index))
        if median_index + 1 < len(self.points):
            self.right.append(
                Node(self.points[median_index + 1:], self.o_axis_index))


if point_count > 0 and query_count > 0:
    queries = (
        ((*islice(it, 2),), (*it,)) for it in
        map(partial(map, int),
            map(methodcaller('split'), islice(stdin, query_count))))
    points = [
        (*it, i) for i, it in
        enumerate(
            map(partial(map, int), map(methodcaller('split'), point_lines)))]
    root = Node(points)

    deque(map(solve_query, queries), maxlen=0)
else:
    print('\n' * query_count, end='')
