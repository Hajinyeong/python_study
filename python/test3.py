one_char = input("하나의 문자 입력")

if one_char == 'R' or one_char == 'r':
    print("Rectangle")
elif one_char == 'T' or one_char == 't':
    print("Triangle")
elif one_char == 'C' or one_char == 'c':
    print("Circle")
else:
    print("Unknown")