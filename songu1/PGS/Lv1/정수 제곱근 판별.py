
import math

def solution(n):
    num=int(math.sqrt(n))
    if num==math.sqrt(n):
        answer = (num+1)**2
    else:
        answer = -1
    return answer