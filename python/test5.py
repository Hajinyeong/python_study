num1 = int(input("첫 번째 정수"))
num2 = int(input("두 번째 정수"))
num3 = int(input("세 번째 정수"))

num_min = 0

if num1 <= num2:
    if num1 <= num3:
        num_min = num1
    else:
        num_min = num3
else:
    if num2 <= num3:
        num_min = num2
    else:
        num_min = num3

print(f"입력된 {num1}, {num2}, {num3} 수중 가장 작은수는 {num_min}이다")