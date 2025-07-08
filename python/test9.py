import random

acc_list = ['+', '-', '*', '/']
sel_acc = acc_list[random.randint(0,3)]

random_number1 = random.randint(0,1000)
random_number2 = random.randint(0,1000)

print(f"선택된 산술은 {sel_acc}입니다.")
print(f"생선된 두 정수는 {random_number1}, {random_number2}입니다.")
print(f"{random_number1}{sel_acc}{random_number2} 의 값울 넣으세요")
your_number = int(input("계산된 정수를 입력하시요 : "))

cal_number = 0
if sel_acc == '+':
    cal_number = random_number1 + random_number2
elif sel_acc == '-':
    cal_number = random_number1 - random_number2
elif sel_acc == '*':
    cal_number = random_number1 * random_number2
elif sel_acc == '/':
    cal_number = random_number1 / random_number2
if cal_number == your_number:
    print("정답")
else:
    print("오답")