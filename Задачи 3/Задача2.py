def replace_repeated_end_symbols(input_string):
    while input_string.endswith(('?', '!')) and input_string[-2] in ('?', '!'):
        input_string = input_string[:-1]

    return input_string


input_text = "Пример текста с вопросами?? и восклицаниями!!!"

result = replace_repeated_end_symbols(input_text)
print(f"Исходный текст: '{input_text}'")
print(f"Текст с одним знаком в конце: '{result}'")