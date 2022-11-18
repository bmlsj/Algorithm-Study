# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1, T + 1):
    sum = 0
    num = list(map(int, input().split()))

    for j in range(10):
        if num[j] % 2:
            sum += num[j]

    print(f"#{test_case} {sum}")
