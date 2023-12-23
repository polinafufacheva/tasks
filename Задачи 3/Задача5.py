def is_surrounded_by_plus(input_string):
    for i in range(len(input_string)):
        if input_string[i].isalpha():
            if i == 0 or i == len(input_string) - 1 or input_string[i - 1] != '+' or input_string[i + 1] != '+':
                return False
            return True

test_string1 = "++A+B+C++"
test_string2 = "+D+E++F+"

result1 = is_surrounded_by_plus(test_string1)
result2 = is_surrounded_by_plus(test_string2)

print(f"Строка '{test_string1}': {result1}")
print(f"Строка '{test_string2}': {result2}")
