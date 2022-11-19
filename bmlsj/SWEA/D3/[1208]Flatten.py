for i in range(10):
    dump = int(input())

    H = list(map(int, input().split()))
    for _ in range(dump):

        max_value = max(H)
        min_value = min(H)
        max_idx = H.index(max_value)
        min_idx = H.index(min_value)

        H[max_idx] -= 1
        H[min_idx] += 1

    result = max(H) - min(H)
    print(f"#{i+1} {result}")
