import random
import time

def typing_game(lives=5, time_limit=2):
    words = ["사과","체리","바나나","딸기","포도","복숭아","수박"]
    score = 0
    print("타이핑 게임 시작! 2초 안에 단어를 입력하세요.")

    while lives > 0:
        word = random.choice(words)
        print(f"\n단어: {word}")
        start = time.time()
        try:
            user_input = input("입력: ")
        except EOFError:
            break
        elapsed = time.time() - start

        if elapsed <= time_limit and user_input.strip() == word:
            score += 1
            print(f" 성공! (+1점) 시간: {elapsed:.2f}s 점수: {score}")
        else:
            lives -= 1
            if elapsed > time_limit:
                print(f"⏱ 시간 초과({elapsed:.2f}s)! 목숨 -1 (남은 목숨: {lives})")
            else:
                print(f" 오답! 입력: '{user_input.strip()}' 목숨 -1 (남은 목숨: {lives})")
    print(f"\n 게임 종료! 최종 점수: {score}")

if __name__ == "__main__":
    typing_game()
