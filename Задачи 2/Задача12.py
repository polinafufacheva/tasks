def create_message(message):
    button_presses = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
        ' ': 0 
}

    result = ""
    for char in message.upper():
        if char in button_presses:
            presses = button_presses[char]
            result += str(presses) * presses 

    return result


your_message = "Hello World"

result_message = create_message(your_message)
print(f"Сообщение для устройства: {result_message}")
