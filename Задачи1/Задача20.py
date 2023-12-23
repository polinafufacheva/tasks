def shortener(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')
        right = st.find(')', left)
        st = st.replace(st[left:right + 1], '')
    return st
print(shortener('Я(лишнее (лишнее) лишнее) играю в баскетбол (лишнее)'))