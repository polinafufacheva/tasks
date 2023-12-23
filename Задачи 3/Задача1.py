def can_share_coins(coins):
    total_coins = sum(coins)

    if total_coins % 3 == 0:
        return True
    else:
        return False

coins_array = [3, 5, 2, 8, 10] 

result = can_share_coins(coins_array)

if result:
    print("Монеты можно поровну распределить между троими детьми.")
else:
    print("Нельзя поровну распределить монеты между троими детьми.")
