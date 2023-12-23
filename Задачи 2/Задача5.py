def multiply_numbers(numbers_string):
    numbers_list = numbers_string.split(', ') 
    result = 1

    for num in numbers_list:
        result *= float(num)

    return result


input_numbers = "2, 3, 4"
result = multiply_numbers(input_numbers)
print(f"Результат умножения чисел из строки '{input_numbers}': {result}")
