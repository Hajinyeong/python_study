total = 0

for i in range(1, 101):  # 1부터 100까지 반복
    if i % 3 == 0:       # 3의 배수인지 확인
        total += i       # 조건에 맞으면 합계에 더함

print("1부터 100 사이 3의 배수의 합:", total)