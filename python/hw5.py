# 사용자로부터 정수 입력 받기
n = int(input("정수를 입력하세요: "))

# 바깥 반복문: 줄 수
for i in range(1, n + 1):
    # 안쪽 반복문: 각 줄에 출력할 * 수
    for j in range(i):
        print('*', end='')
    print()  # 줄바꿈
 





