num = int(input("정수를 입력하세요: "))

print(f"{num}의 약수는 다음과 같습니다:")

# 1부터 num까지 반복하면서 약수 찾기
for i in range(1, num + 1):
    if num % i == 0:
        print(i)