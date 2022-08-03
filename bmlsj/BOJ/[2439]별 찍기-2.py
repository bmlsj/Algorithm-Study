# for문 예제2
n = int(input())

# 1번
for i in range(1, 1+n):
    for j in range(n-i, 0, -1):
        print(" ", end='')
    print("*"*i)

# 2번
for i in range(n):
    print(" "*(n-i), end='')
    print("*"*(i+1))