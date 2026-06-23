import random
def run_quiz():
    quiz_bank = {
        "실시간으로 시스템 부하와 프로세스 목록을 동적으로 모니터링하는 명령어는?": "top",
        "실행하는 그 순간 시스템에 존재하는 프로세스의 정적 스냅샷을 보여주는 명령어는?": "ps",
        "현재 터미널 세션 내부에서 백그라운드로 실행 중이거나 정지된 작업 목록을 보여주는 명령어는?": "jobs",
        "특정 프로세스나 작업에 시그널을 보내 종료하거나 제어하는 명령어는?": "kill"
    }
    questions = list(quiz_bank.keys())
    random.shuffle(questions)
    score = 0
    lives = 3
    print("=" * 50)
    print("리눅스 프로세스 관리 명령어 퀴즈 게임")
    print("인풋창에 'hint'를 입력하면 명령어의 글자 수를 알려줍니다!")
    print("=" * 50)
    for q in questions:
        if lives <= 0:
            break
        correct_answer = quiz_bank[q]
        while True:
            print(f"\n[질문] {q}")
            user_input = input("정답을 입력하세요 (또는 'hint' 입력): ").strip().lower()
            if user_input == 'hint':
                print(f"[힌트] 이 명령어는 총 {len(correct_answer)}글자입니다.")
                continue
            if user_input == correct_answer:
                print("정답입니다!")
                score += 25
                break
            else:
                lives -= 1
                print(f"틀렸습니다! (남은 기회: {lives}번)")
                break
    print("\n" + "=" * 50)
    print("게임 종료! 최종 결과를 출력합니다.")
    print(f"최종 점수: {score}점 / 100점")
    print(f"남은 목숨: {lives}개")
    if score == 100:
        print("[리눅스 마스터] 완벽합니다! 모든 명령어를 숙지하셨군요.")
    elif score >= 50:
        print("[리눅스 주니어] 조금만 더 연습하면 완벽해질 것입니다.")
    else:
        print("[리눅스 초보자] 첫 번째 과제 README를 다시 읽어보세요!")
    print("=" * 50)
if __name__ == "__main__":
    run_quiz()
