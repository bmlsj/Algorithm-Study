# 한줄에 하나씩 주어진 자연수들 중 최대값을 출력하고 최대값이 몇번째인지 출력
import sys
data=[]

for i in range(0,9):
    data.append(int(sys.stdin.readline().rstrip()))

m=max(data)
print(m)
print(data.index(m)+1)