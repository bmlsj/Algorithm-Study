# 틀린 문제 ㅠㅠ
from itertools import permutations


T = int(input())

for i in range(1, T + 1):

    num, change = input().split()  # 숫자 정보, 교환 횟수
    change = int(change)

    now = [num]
    nxt = []

    for _ in range(change):
        while now:
            s = list(map(int, now.pop()))
        nxt = list(max(permutations(s)))

    result = [*nxt]
    result = ''.join(map(str, result))
    print(f"#{i} {int(result)}")
