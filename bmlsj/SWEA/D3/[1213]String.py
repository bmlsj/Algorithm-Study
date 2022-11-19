# import sys
# sys.stdin = open("input.txt", 'rt', encoding='UTF8')

for i in range(10):
    N = int(input())
    find = input()
    S = input()

    count = S.count(find)
    print(f"#{i+1} {count}")
