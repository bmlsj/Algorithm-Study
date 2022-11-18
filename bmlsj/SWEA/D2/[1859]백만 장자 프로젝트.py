# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1

T = int(input())

for i in range(1, T + 1):
    N = int(input())
    N_list = list(map(int, input().split()))

    max_value = N_list[-1]
    profit = 0

    for j in range(N - 2, -1, -1):
        if max_value <= N_list[j]:
            max_value = N_list[j]

        else:
            profit += (max_value - N_list[j])

    print("#{} {}".format(i, profit))
