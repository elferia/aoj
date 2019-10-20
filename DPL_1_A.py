amount, coin_kind_count = [int(s) for s in input().split()]
coin_kinds = [1]
coin_kinds.extend(n for n in map(int, input().split()) if 1 < n <= amount)

min_coin_count = list(range(amount + 1))


def ith_amount_min_coin_count(i: int, current_amount: int) -> int:
    ith_value = coin_kinds[i]
    if ith_value == current_amount:
        return 1

    without_ith_count = min_coin_count[current_amount]
    return min(
        without_ith_count, min_coin_count[current_amount - ith_value] + 1)


for i in range(1, len(coin_kinds)):
    for current_amount in range(coin_kinds[i], amount + 1):
        min_coin_count[current_amount] = ith_amount_min_coin_count(
            i, current_amount)

print(min_coin_count[amount])
