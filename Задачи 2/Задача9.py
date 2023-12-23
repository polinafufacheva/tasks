def accumulate_numbers(input_list):
    accumulated_list = []
    cumulative_sum = 0

    for num in input_list:
        cumulative_sum += num
        accumulated_list.append(cumulative_sum)

    return accumulated_list

numbers = [1, 2, 3, 4, 5]
result = accumulate_numbers(numbers)
print(f"Исходный список: {numbers}")
print(f"Массив с накопленными суммами: {result}")
