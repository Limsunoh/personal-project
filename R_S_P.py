import random

R_S_P = ["가위", "바위", "보"]

print("가위바위보 게임을 시작합니다.")

win_count = 0
lose_count = 0
draw_count = 0

while True:
    try:
        human = str(input("가위, 바위, 보 중 하나를 선택하세요")).strip()

        if human != "가위" and human != "바위" and human != "보":
            print("가위, 바위, 보만 입력하세요")
            continue

        c_choice = random.choice(R_S_P)
        print(f"컴퓨터의 선택은 {c_choice} 입니다~")

        if (human == "가위" and c_choice == "바위") or \
                (human == "바위" and c_choice == "보") or \
                (human == "보" and c_choice == "가위"):
            print("당신이 졌습니다.")
            lose_count += 1

        elif (human == "가위" and c_choice == "보") or \
                (human == "바위" and c_choice == "가위") or \
                (human == "보" and c_choice == "바위"):
            print("당신이 이겼습니다.")
            win_count += 1

        else:
            print("비겼습니다.")
            draw_count += 1

        while True:
            replay = input("다시 하시겠습니까? y/n").strip().lower()
            if replay != 'n' and replay != 'y':
                print('y'" 혹은 "'n'"을 입력하세요.")
            elif replay == 'y':
                break
            else:
                print("게임을 종료합니다.")
                print(f"승: {win_count} 패: {lose_count} 무승부: {draw_count}")
                exit()

    except ValueError:
        print("똑바로 입력하세요")
