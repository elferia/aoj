from array import array

amount, coin_kind_count = [int(s) for s in input().split()]
coin_kinds = array('H', (n for n in map(int, input().split()) if n <= amount))


def min_coin_count(coin_index_stop: int, current_amount: int) -> int:
    if coin_index_stop == 0 or current_amount < 0:
        return amount + 1

    if current_amount == 0:
        return 0

    return min(
        min_coin_count(
            coin_index_stop, current_amount - coin_kinds[coin_index_stop - 1]
        ) + 1, min_coin_count(coin_index_stop - 1, current_amount))


print(min_coin_count(len(coin_kinds), amount))
