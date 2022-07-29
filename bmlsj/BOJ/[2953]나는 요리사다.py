# 2차원 배열 사용 예제

human = [list(map(int, input().split())) for _ in range(5)]
score = [0] * 5
max_score = 0

for i in range(5):
    sum = 0
    for j in range(4):
        sum += human[i][j]
    
    score[i] = sum
    max_score = max(score)

for i in range(5):
    if score[i] == max_score:
        print(i+1, max_score)