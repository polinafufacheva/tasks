def count_lucky_numbers(length):
    def generate_numbers(num, sum_left, sum_right, length):
        if length == 0:
            return sum_left == sum_right
        count = 0
        for i in range(num if num != -1 else 1, 10):
            count += generate_numbers(i, sum_left + i, sum_right, length - 1)
            count += generate_numbers(i, sum_left, sum_right + i, length - 1)
        return count

    if length <= 0:
        return 0
    return generate_numbers(-1, 0, 0, length // 2)

length = 4

result = count_lucky_numbers(length)
print(f"Количество 'счастливых' чисел длины {length}: {result}")