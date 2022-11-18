# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QPsXKA2UDFAUq&categoryId=AV5QPsXKA2UDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

num = list(map(int, input().split()))
num = sorted(num)
print(num[((T + 1) // 2) - 1])
