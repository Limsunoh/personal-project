import random

best = False
print("업다운 게임을 시작합니다!")

while True:
    random_number = random.randint(1, 100)
    seek = 0
    print(f"현재 최고기록: {best if best != False else '최고 기록 없음'}")

    try:
        while True:
            seek += 1
            if seek == 1:
                human = int(input("마음에 드는 숫자를 입력하세요: "))
            else:
                human = int(input("다시 입력하세요"))

            if 1 > human or 100 < human:
                print("1에서 100 사이의 숫자를 입력하세요")
                continue

            if human > random_number:
                print("다운 입니다.")
            elif human < random_number:
                print("업 입니다.")
            else:
                print("정답입니다~")
                print(f"{seek}번만에 맞추셨습니다~")

                if best is False or seek < best:
                    best = seek
                    print(f"NEW 최고기록:{seek}")
                else:
                    print(f"기존 최고기록:{best}")

                break

    except ValueError:
        print("숫자를 입력하세요.")

    replay = input("다시 하시겠습니까? y/n: ").strip().lower()
    if replay != 'y':
        print("게임을 종료합니다.")
        break
