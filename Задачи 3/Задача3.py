def is_busted(card_values):
    total_sum = sum(card_values)

    if total_sum > 21:
        return True
    else:
        return False

cards = [10, 5, 7]

result = is_busted(cards)
print(f"Сумма карт: {sum(cards)}")
print(f"Перебор: {result}")