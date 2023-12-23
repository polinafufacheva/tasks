def remove_extra_spaces(input_string):
    input_string = input_string.strip()
    input_string = ' '.join(input_string.split())
    return input_string
input_str = " Эта строка имеет лишние пробелы "
result = remove_extra_spaces(input_str)
print(f"Исходная строка: '{input_str}'")
print(f"Строка без лишних пробелов: '{result}'")