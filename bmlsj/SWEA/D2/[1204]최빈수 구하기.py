
T = int(input())


for i in range(1, T+1):
    N = int(input())  # 테스트 케이스 번호

    grades = list(map(int, input().split()))
    max_value = grades[0]
    max_count = grades.count(max_value)

    for n in grades:
        count = grades.count(n)
        if max_count < count:
            max_count = count
            max_value = n

    print(f"#{N} {max_value}")
