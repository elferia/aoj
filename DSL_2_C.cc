#include <algorithm>
#include <array>
#include <cassert>
#include <cinttypes>
#include <cstdint>
#include <cstdio>
#include <deque>
#include <iostream>
#include <iterator>
#include <list>
#include <string>
#include <utility>
#include <vector>

namespace {
struct Point
{
    Point(int_fast32_t x, int_fast32_t y, uint_fast32_t index)
      : coordinate{ x, y }
      , index(index)
    {}

    const std::array<const int_fast32_t, 2> coordinate;
    const uint_fast32_t index;
};

using AxisRange = std::pair<int_fast32_t, int_fast32_t>;
using Range = std::array<AxisRange, 2>;

struct Node
{
    explicit Node(const std::vector<Point>& points)
      : axis_index(0)
      , point(nullptr)
      , left(nullptr)
      , right(nullptr)
    {
        std::transform(points.cbegin(),
                       points.cend(),
                       std::back_inserter(this->points),
                       [](const auto& p) { return &p; });
    }

    template<class It>
    Node(It b, It e, uint_fast8_t axis_index)
      : axis_index(axis_index)
      , point(nullptr)
      , left(nullptr)
      , right(nullptr)
      , points(std::vector<const Point*>(b, e))
    {}

    void search(int_fast32_t, int_fast32_t, int_fast32_t, int_fast32_t);
    int_fast32_t search(const Range& range, std::deque<Node*>& queue);
    void setUp();
    const uint_fast8_t axis_index;
    const Point* point;
    Node* left;
    Node* right;
    std::vector<const Point*> points;
};
} // namespace

int
main()
{
    uint_fast32_t point_count = 0;
    int ret = std::scanf("%" SCNuFAST32, &point_count);
    assert(ret == 1);

    std::vector<Point> points;
    for (uint_fast32_t i = 0; i < point_count; ++i) {
        int_fast32_t x = 0;
        int_fast32_t y = 0;
        ret = std::scanf("%" SCNdFAST32 " %" SCNdFAST32, &x, &y);
        assert(ret == 2);

        points.emplace_back(x, y, i);
    }

    uint_fast16_t query_count = 0;
    ret = std::scanf("%" SCNuFAST16, &query_count);
    assert(ret == 1);

    if (point_count == 0) {
        std::cout << std::string(query_count, '\n');
    } else {
        Node root(points);
        for (uint_fast16_t i = 0; i < query_count; ++i) {
            int_fast32_t sx = 0;
            int_fast32_t tx = 0;
            int_fast32_t sy = 0;
            int_fast32_t ty = 0;
            ret = std::scanf("%" SCNdFAST32 " %" SCNdFAST32 " %" SCNdFAST32
                             " %" SCNdFAST32,
                             &sx,
                             &tx,
                             &sy,
                             &ty);
            assert(ret == 4);

            root.search(sx, tx, sy, ty);
            std::printf("\n");
        }
    }

    return 0;
}

namespace {
void
Node::search(int_fast32_t sx, int_fast32_t tx, int_fast32_t sy, int_fast32_t ty)
{
    const Range range{ AxisRange(sx, tx), AxisRange(sy, ty) };
    std::list<uint_fast32_t> answer;
    std::deque<Node*> queue(1, this);
    while (!queue.empty()) {
        const auto i = queue.front()->search(range, queue);
        queue.pop_front();
        if (i >= 0) {
            answer.push_back(static_cast<decltype(answer)::value_type>(i));
        }
    }

    answer.sort();
    std::string ss;
    for (const auto& i : answer) {
        char s[6 + 1 + 1];
        std::snprintf(s, sizeof s, "%" PRIuFAST32 "\n", i);
        ss += s;
    }
    std::cout << ss;
}

int_fast32_t
Node::search(const Range& range, std::deque<Node*>& queue)
{
    const auto s0 = range[axis_index].first;
    const auto t0 = range[axis_index].second;

    if (point == nullptr) {
        setUp();
    }

    const auto p0 = point->coordinate[axis_index];

    if (t0 < p0) {
        if (left) {
            queue.push_back(left);
        }
        return -1;
    }

    const uint_fast8_t o_axis_index = (axis_index + 1) % 2;
    const auto s1 = range[o_axis_index].first;
    const auto t1 = range[o_axis_index].second;
    const auto p1 = point->coordinate[o_axis_index];
    const auto index = static_cast<int_fast32_t>(point->index);
    if (p0 <= s0) {
        if (right) {
            queue.push_back(right);
        }
        return p0 == s0 && s1 <= p1 && p1 <= t1 ? index : -1;
    }

    if (left) {
        queue.push_back(left);
    }
    if (right) {
        queue.push_back(right);
    }
    return s1 <= p1 && p1 <= t1 ? index : -1;
}

void
Node::setUp()
{
    std::sort(
      points.begin(), points.end(), [this](const auto& a, const auto& b) {
          return a->coordinate[axis_index] < b->coordinate[axis_index];
      });

    const auto median_index = points.size() / 2;
    auto median_it = std::lower_bound(
      points.cbegin(),
      points.cbegin() +
        static_cast<decltype(points)::difference_type>(median_index),
      points.at(median_index)->coordinate[axis_index],
      [this](const auto& point, const auto& value) {
          return point->coordinate[axis_index] < value;
      });

    point = *median_it;
    const uint_fast8_t o_axis_index = (axis_index + 1) % 2;
    if (median_it != points.cbegin()) {
        left = new Node(points.cbegin(), median_it, o_axis_index);
    }
    if (++median_it != points.cend()) {
        right = new Node(median_it, points.cend(), o_axis_index);
    }
}
} // namespace
