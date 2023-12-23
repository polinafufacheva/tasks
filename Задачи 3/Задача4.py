def sum_numbers_in_string(input_string):
    current_number = ''
    total_sum = 0

    for char in input_string:
        if char.isdigit():
            current_number += char
        elif current_number:
            total_sum += int(current_number)
            current_number = ''

    if current_number:
        total_sum += int(current_number)

    return total_sum

input_str = "abc123def45gh6i7"

result = sum_numbers_in_string(input_str)
print(f"Исходная строка: '{input_str}'")
print(f"Сумма чисел в строке: {result}")
