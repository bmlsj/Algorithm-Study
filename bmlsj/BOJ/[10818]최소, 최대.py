# ArrayList를 사용하는 예제

n = int(input())
a_list = list(map(int, input().split()))

# 함수 사용
print(min(a_list), max(a_list))

# 함수 사용X
max_num = a_list[0]
min_num = a_list[0]

for num in a_list:
    if max_num < num:
        max_num = num
    if min_num > num:
        min_num = num

print( min_num, max_num)