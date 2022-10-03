def solution(n):
    arr=[n]
    for i in range(1,n):
        if(n%i==0):
            arr.append(i)
    answer = sum(arr)
    return answer