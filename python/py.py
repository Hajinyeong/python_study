import time
import random

sentences =[
    "나는 파이썬을 배우고 있어요",
    "타자 속도를 테스트 해볼까요?",
    "오늘 날씨는 정말 좋네요",
    "프로그래밍은 재밌어요",
    "천 리 길도 한 걸음부터",
]

print("타자 속도 테스트 게임입니다!")
input("엔터를 누르면 문장이 나옵니다...")

target = random.choice(sentences)
print("\n다음 문장으 그대로 입력하세요:\n")
print(f"{target}\n")

input("준비되면 Enter를 누르세요!")

start_time = time.time()
mistake= 0

while True:
    typed = input("\n입력: ")


    correct = 0
        for i in range(min(len(target), len(typed))):
            if target[1] == typed[i]:
                correct +=1

    total = max(len(target), len(typed))
    accuracy = correct / total * 100
    if accuracy == 100
        print("\n오타가 있습니다. 다시 시도하세요.")
        mistake += 1

end_time = time.time()
elapsed = end_times - start_time
speed = len(typed) / elapsed*60

print("\n결과")
print(f"걸린시간": {elspeeed:.2f}초")
print(f"오타횟수": {mistake}")
print(f"타자 속도":{sped:.2f} 자/분")



