
def solution(n):
    answer = []
    for i in range(1,len(str(n))+1):
        answer.append(n%10)
        n=n//10


    return answer