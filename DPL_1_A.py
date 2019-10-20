from array import array

amount, coin_kind_count = [int(s) for s in input().split()]
coin_kinds = array('H', [1])
coin_kinds.extend(n for n in map(int, input().split()) if 1 < n <= amount)

min_coin_count = [array('H', range(amount + 1))]


def ith_amount_min_coin_count(i: int, current_amount: int) -> int:
    ith_value = coin_kinds[i]
    if ith_value == current_amount:
        return 1

    without_ith_count = min_coin_count[i - 1][current_amount]
    if ith_value > current_amount:
        return without_ith_count

    return min(
        without_ith_count, min_coin_count[i][current_amount - ith_value] + 1)


for i in range(1, len(coin_kinds)):
    min_coin_count.append(array('H', [0]))
    for current_amount in range(1, amount + 1):
        min_coin_count[-1].append(ith_amount_min_coin_count(i, current_amount))

print(min_coin_count[len(coin_kinds) - 1][amount])
