CASE_FUNCTIONS = [str.upper, str.lower]

def camel(st):

    index = 0
    camel_st = ''
    for sym in st:
        if sym.isalpha():
            camel_st += CASE_FUNCTIONS[index % 2](sym)
            index += 1
        else:
            camel_st += sym

    return camel_st

print(camel('Я играю в баскетбол'))