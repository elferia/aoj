amount, coin_kind_count = [int(s) for s in input().split()]
coin_kinds = [1]
coin_kinds.extend(n for n in map(int, input().split()) if 1 < n <= amount)

min_coin_count = list(range(amount + 1))


for i in range(1, len(coin_kinds)):
    ith_value = coin_kinds[i]
    min_coin_count[ith_value] = 1
    for current_amount in range(ith_value + 1, amount + 1):
        use_ith_count = min_coin_count[current_amount - ith_value] + 1
        if use_ith_count < min_coin_count[current_amount]:
            min_coin_count[current_amount] = use_ith_count

print(min_coin_count[-1])
