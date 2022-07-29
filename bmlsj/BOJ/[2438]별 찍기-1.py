# for문 예제1

a = int(input())

# for문
for i in range(a):
    print("*"*(i+1))

# 2중 for문
for i in range(a):
    for j in range(i+1):
        print('*', end='')
    print()