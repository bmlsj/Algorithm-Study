# 본인 점수/최고점*100한 점수로 조작하여 평균점수 출력

# 함수 사용해서 시간 줄이기
import sys
N=int(input())
data=list(map(int,sys.stdin.readline().split()))
m=max(data)
for i in range(N):
    data[i]=data[i]/m*100
print(sum(data)/N)