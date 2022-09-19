# 배열의 원소들 중 최대값, 최소값 출력

import sys
n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))

print(min(num),max(num))