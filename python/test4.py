radius = float(input("원의 반지름을 입력하시오"))

if radius < 0:
    print("잘못된 입력값입니다.")
else:
    area = 3.14*radius**2
    print(f"입력된 반지름 {radius}의 넓이는 {area}입니다.")