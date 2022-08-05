# O,X로 OX퀴즈의 결과.
# O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 됨
# 점수를 출력하기

# add(더하는 숫자)와 score(총 합)을 따로 구하여 풀기
import sys
N=int(input())

for i in range(N):
    data=sys.stdin.readline().rstrip()
    (score,add)=(0,0)
    for j in range(len(data)):
        if data[j]=='X':
            add=0
            continue
        elif data[j]=='O':
            add+=1
            score+=add
    print(score)

