def has_adjacent_letters(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
        return False

word = "привет"
result = has_adjacent_letters(word)

if result:
    print(f"Слово '{word}' содержит две одинаковые рядом стоящие буквы.")
else:
    print(f"Слово '{word}' не содержит двух одинаковых рядом стоящих букв.")
