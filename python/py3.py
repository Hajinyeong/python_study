import random

proverbs = [
    ("호랑이굴에", "들어가야 산다"),
    ("등잔 밑이", "어둡다"),
    ("가는 말이", "고와야 오는 말이 곱다"),
    ("고생끝에", "낙이온다"),
    ("원숭이도", "나무에서 떨어진다."),
    ("티끌모아", "태산"),
    ("백문이","불여일견"),
    ("똥 묻은개가","겨묻은 나무가도니다"),
]

import qrcode
img=qrcode.make("<String>")
img.save("qrcode.png")

img = qrcode.make("answer")
img.save("answer_qr.png")

while True:
    quserion, answer = random,choice(proverbs)
    print(f"\n오늘의 퀴즈: {question}_____")

    img = qrcode.make(answer)
    img.save9("answer_qr.png")
    print("정답 QR코드가 'answer_qr.png'로 저장되었습니다.")
    
    again = input("계속하려면 y, 종려하려면 n:").strip().lower()
if again ! = 'y':
    print("프로그램을 종료합니다.")
    break

