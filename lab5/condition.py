score = float(input("학점 입력> "))

# (최소 점수, 별명) 순서로 배치 (내림차순)
grades = [
    (4.5, "신"),
    (4.2, "교수님의 사랑"),
    (3.5, "현 체제의 수호자"),
    (2.8, "일반인"),
    (2.3, "일탈을 꿈꾸는 소시민"),
    (1.75, "오락문화의 선구자"),
    (1.0, "불가촉천민"),
    (0.5, "자벌레")
]

# 위에서부터 차례대로 비교하며 해당하면 바로 출력 후 종료
for min_score, nickname in grades:
    if score >= 0.5:
        pass
    elif score > 0 :
        print("플랑크톤")
        break
    else :
        print("시대를 앞서가는 혁명의 씨앗")
    if score >= min_score:
        print(nickname)
        break