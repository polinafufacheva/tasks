def reverse_string(input_string):
    reversed_str = input_string[::-1] 
    reversed_str = reversed_str.swapcase() 

    return reversed_str

original_string = "Hello World!"
reversed_result = reverse_string(original_string)
print(f"Исходная строка: {original_string}")
print(f"Перевернутая строка с измененным регистром: {reversed_result}")
