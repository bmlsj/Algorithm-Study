# 삽입과 삭제가 빈번해 ArrayList 사용시 시간초과
# stack & pop 사용

# arrayList 시
"""
n, k = map(int, input().split())
n_list = list(input())

max = n_list[0]
for i in range(len(n_list)):
    while n_list[i] > n_list[i-1] and k:
        k -= 1
        del n_list[i-1]
        n_list.insert(0, 'f')
    
ans = ' '
for i in range(len(n_list)-k):
    if n_list[i] != 'f':
        ans += n_list[i]

print(ans)
"""

