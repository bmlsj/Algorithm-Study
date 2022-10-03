def solution(n):
    answer = 0
    arr=[int(i) for i in str(n)]
    arr.sort()
    for i in range(0,len(arr)):
        arr[i]*=10**i
    answer=sum(arr)
    return answer