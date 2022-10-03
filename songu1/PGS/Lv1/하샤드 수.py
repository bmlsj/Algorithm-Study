
def solution(x):
    arr=[int(i) for i in str(x)]
    if x % sum(arr):
        answer=False
    else:
        answer=True

    return answer