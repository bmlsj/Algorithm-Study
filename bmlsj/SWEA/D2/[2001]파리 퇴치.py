T = int(input())

for i in range(T):
    n, m = map(int, input().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    sum_value = []
    m_list = []
    for j in range(n - (m - 1)):
        for k in range(n - (m - 1)):
            m_list.clear()
            for p in range(m):

                for q in range(m):
                    m_list.append(arr[j + p][k + q])

            sum_value.append(sum(m_list))

    print(f"#{i + 1} {max(sum_value)}")
