for i in range(10):
    N = int(input())  # 건물의 개수

    # 2차원 배열 초기화
    arr = []
    for _ in range(N):
        arr.append([0] * 255)

    H = list(map(int, input().split()))  # 건물의 길이

    for j in range(N):  # 세로
        col = H[j]
        for k in range(col):
            arr[j][k] = 1

    cnt = 0
    # 1 이면 위, 아래 조건 확인
    for j in range(N):
        for k in range(255):
            if arr[j][k] == 1:
                if arr[j - 2][k] == 0 and arr[j - 1][k] == 0 and arr[j + 1][k] == 0 and arr[j + 2][k] == 0:
                    cnt += 1

    print(f"#{i+1} {cnt}")
