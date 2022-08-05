# A*B*C한 결과에 0~9까지의 숫자가 몇번 쓰였는지 출력
import sys
res=1
for i in range(3):
    res*=int(sys.stdin.readline())
res=str(res)

for i in range(10):
    print(res.count(str(i)))