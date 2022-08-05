# 한줄에 하나씩 주어진 숫자들을 42로 나누었을때 서로 다른 나머지가 몇개있는지

# 리스트에서 서로 다른 값이 몇개인지 -> 리스트를 세트로 바꿔서 길이 구하기

import sys
data=[]
count=0

for i in range(10):
    data.append(int(sys.stdin.readline().rstrip())%42)

print(len(set(data)))
