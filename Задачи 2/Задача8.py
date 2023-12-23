def encode_string(input_string):
    encoded_string = ""
    for char in input_string:
        if char.lower() == 'a':
            encoded_string += '3'
        elif char.lower() == 'e':
            encoded_string += '×'
        elif char.lower() == 'i':
            encoded_string += '4'
        elif char.lower() == 'o':
            encoded_string += 'к'
        elif char.lower() == 'u':
            encoded_string += 'р'
        else:
            encoded_string += char

    return encoded_string

input_str = "Hello, World!"
encoded_result = encode_string(input_str)
print(f"Закодированная строка: {encoded_result}")
