for i in range(10):
    N = int(input())

    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    # 열의 합
    col = []
    max_col = 0
    for j in range(100):
        col.append(sum(arr[j]))

    max_col = max(col)

    # 행의 합
    row = []
    max_row = 0
    for j in range(100):
        row_sum = 0  # 새 행에 들어가기 전에 초기화 해주기
        for k in range(100):
            row_sum += arr[k][j]
        row.append(row_sum)
        max_row = max(row)

    # 대각선1의 합
    digo1_sum = 0
    digo1 = []
    for j in range(100):
        for k in range(100):
            if j == k:
                digo1_sum += arr[j][k]

        digo1.append(digo1_sum)

    """
    이중 for문을 쓰지 않아도 된다.
    for i in range(100):
        sum += arr[i][i]
    """

    # 대각선 합2
    digo2_sum = 0
    digo2 = []

    for j in range(100):
        for k in range(100):
            if i + k == 99:
                digo2_sum += arr[j][k]
        digo2.append(digo2_sum)

    result = [max_row, max_col, digo1_sum, digo2_sum]
    print(f"#{i + 1} {max(result)}")
