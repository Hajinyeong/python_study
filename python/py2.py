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
front,back=random.choice(proverbs)


print(f"속담:\"{front}____\"")
amswer = input("뒷부분을 입력하세요: ").strip()

#if 입력값  == 정답:
#    print("정답입니다!n")
#    score+=1
#else:
#    print(f"오답입니다.정답은:\"{back}\"\n")

total +=1

if  answer == back:
    print("정답입니다!\n")
    score +=1
else:
    print(f"오답입니다. 정답은: \"{back}\"\n")

#for total in 범주(n):
    #문제 선택 및 정답 가져오기
    #if 입력값 == 정답:
        #print9("정답입니다!\n")
        #score +=1
#else:
    #print(f"오답입니다.정답은:\"{back}\"\n")
for totla in range(5):
    front, back=random,choice(peverbs)

    print(f"속담;\"{fornt}____\"")
    answer = input("뒷부분을 입력하세요:").strip()

    if answer == back:
        print("정답입니다!\n")
        score +=1
    else:
        hint = back[0]
        length = len(back)
        print(f"오답입니다. 힌트:'{ hint}'로 시작해요. (총 {length}글자)")
        answer = input("힌트를 보고 다시 입력하세요:").strip()
        if answer == back:
            print("정답입니다!\n")
            score += 1
        else:
            print(f"오답입니다. 정답은:\"{back}\"\n")
        
    
total +=1
print(f"\n게임종료! 당신의 총{total} 중 {score}맞추었습니다!")