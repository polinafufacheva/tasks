def is_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            return False
    return True

array1 = [1, 2, 3, 4, 5]
array2 = [1, 3, 2, 5, 7]

result1 = is_ascending(array1)
result2 = is_ascending(array2)

print(f"Числа в массиве {array1} возрастают: {result1}")
print(f"Числа в массиве {array2} возрастают: {result2}")