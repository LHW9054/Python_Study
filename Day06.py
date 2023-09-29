# 조건문, 반복문, 입력/출력 등 다양한 구문을 활용
# 성적 평균 계산하기

print("===성적 평균 계산하기===")
num_of_scores = int(input("몇 개의 점수를 입력하시겠습니까? "))

scores = []
for i in range(num_of_scores):
    score = float(input(f"과목 {i + 1}의 점수를 입력하세요: "))
    scores.append(score)

total_score = sum(scores)
average_score = total_score / num_of_scores
print(f"평균 성적은 {average_score:.2f}입니다.")