from collections import deque

amount, coin_kind_count = [int(s) for s in input().split()]
coin_kinds = (n for n in map(int, input().split()) if 1 < n <= amount)

min_coin_count = list(range(amount + 1))


def update_min_coin_count(ith_value: int) -> None:
    min_coin_count[ith_value] = 1
    for current_amount in range(ith_value + 1, amount + 1):
        use_ith_count = min_coin_count[current_amount - ith_value] + 1
        if use_ith_count < min_coin_count[current_amount]:
            min_coin_count[current_amount] = use_ith_count


deque(map(update_min_coin_count, coin_kinds), maxlen=0)
print(min_coin_count[-1])
