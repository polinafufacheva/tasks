def find_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 0:
        mid = length // 2
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
            mid = length // 2
            median = sorted_numbers[mid]
    return median

array1 = [1, 3, 5, 7, 9]
array2 = [2, 4, 6, 8]

result1 = find_median(array1)
result2 = find_median(array2)

print(f"Медиана ряда чисел {array1}: {result1}")
print(f"Медиана ряда чисел {array2}: {result2}")
